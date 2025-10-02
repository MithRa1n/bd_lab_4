import os
from http import HTTPStatus
import secrets
import jwt
import datetime
from typing import Dict, Any
from functools import wraps

from flask import Flask, jsonify, request, g
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

db = SQLAlchemy()
todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}
    
    CORS(app)
    _init_db(app)
    register_routes(app)
    _init_swagger(app)

    return app


def _init_swagger(app: Flask) -> None:
    authorizations = {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'JWT Token. Format: Bearer <token>'
        }
    }
    
    api = Api(
        app, 
        title='Pizza Delivery Management API',
        description='Complete REST API for pizza delivery management system with authentication',
        version='2.0',
        doc='/api/docs/',
        prefix='/api/v1',
        authorizations=authorizations,
        security='Bearer'
    )
    
    user_model = api.model('User', {
        'id': fields.Integer(description='User ID'),
        'username': fields.String(required=True, description='Username'),
        'email': fields.String(required=True, description='Email'),
        'phone': fields.String(description='Phone number'),
        'address': fields.String(description='Delivery address')
    })
    
    pizza_model = api.model('Pizza', {
        'id': fields.Integer(description='Pizza ID'),
        'name': fields.String(required=True, description='Pizza name'),
        'description': fields.String(description='Pizza description'),
        'price': fields.Float(required=True, description='Price'),
        'size': fields.String(description='Size (Small/Medium/Large)'),
        'ingredients': fields.List(fields.String, description='Ingredients')
    })
    
    order_model = api.model('Order', {
        'id': fields.Integer(description='Order ID'),
        'user_id': fields.Integer(required=True, description='User ID'),
        'pizzas': fields.List(fields.Nested(pizza_model), description='Pizza list'),
        'total_price': fields.Float(description='Total price'),
        'status': fields.String(description='Order status'),
        'delivery_address': fields.String(description='Delivery address'),
        'created_at': fields.DateTime(description='Creation time')
    })
    
    login_model = api.model('Login', {
        'username': fields.String(required=True, description='Username'),
        'password': fields.String(required=True, description='Password')
    })
    
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                api.abort(401, 'Token is missing!')
            
            try:
                if token.startswith('Bearer '):
                    token = token[7:]
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
                g.current_user = data['username']
            except:
                api.abort(401, 'Invalid token!')
            
            return f(*args, **kwargs)
        return decorated
    
    users_db = {
        'admin': {
            'id': 1,
            'username': 'admin',
            'email': 'admin@pizza.com',
            'password': generate_password_hash('admin123'),
            'phone': '+380123456789',
            'address': '123 Main St'
        },
        'user': {
            'id': 2,
            'username': 'user',
            'email': 'user@gmail.com', 
            'password': generate_password_hash('user123'),
            'phone': '+380987654321',
            'address': '456 Oak Ave'
        }
    }
    
    pizzas_db = {
        1: {'id': 1, 'name': 'Margherita', 'description': 'Classic pizza with tomatoes and mozzarella', 'price': 299.0, 'size': 'Medium', 'ingredients': ['tomatoes', 'mozzarella', 'basil']},
        2: {'id': 2, 'name': 'Pepperoni', 'description': 'Pizza with pepperoni and cheese', 'price': 349.0, 'size': 'Large', 'ingredients': ['pepperoni', 'mozzarella', 'tomato sauce']},
        3: {'id': 3, 'name': 'Vegetarian', 'description': 'Pizza with vegetables', 'price': 319.0, 'size': 'Medium', 'ingredients': ['bell peppers', 'mushrooms', 'onions', 'tomatoes']}
    }
    
    orders_db = {}
    order_counter = 1
    
    ns_auth = api.namespace('auth', description='Authentication and authorization')
    ns_users = api.namespace('users', description='User management')
    ns_pizzas = api.namespace('pizzas', description='Pizza catalog')
    ns_orders = api.namespace('orders', description='Order management')
    ns_health = api.namespace('health', description='System monitoring')
    
    @ns_auth.route('/register')
    class Register(Resource):
        def post(self):
            """Register new user"""
            data = request.get_json()
            username = data.get('username')
            
            if username in users_db:
                api.abort(400, f'User {username} already exists')
            
            users_db[username] = {
                'id': len(users_db) + 1,
                'username': username,
                'email': data.get('email'),
                'password': generate_password_hash(data.get('password')),
                'phone': data.get('phone', ''),
                'address': data.get('address', '')
            }
            
            return {'message': f'User {username} registered successfully!'}, 201
    
    @ns_auth.route('/login')
    class Login(Resource):
        @api.expect(login_model)
        def post(self):
            """Login and get JWT token"""
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            user = users_db.get(username)
            if not user or not check_password_hash(user['password'], password):
                api.abort(401, 'Invalid credentials')
            
            token = jwt.encode({
                'username': username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            
            return {
                'token': token,
                'user': {
                    'id': user['id'],
                    'username': user['username'],
                    'email': user['email']
                },
                'message': 'Login successful!'
            }
    
    @ns_users.route('/profile')
    class UserProfile(Resource):
        @api.doc(security='Bearer')
        @token_required
        @api.marshal_with(user_model)
        def get(self):
            """Get current user profile"""
            user = users_db.get(g.current_user)
            if not user:
                api.abort(404, 'User not found')
            return user
    
    @ns_users.route('/')
    class UsersList(Resource):
        @api.doc(security='Bearer')
        @token_required
        @api.marshal_list_with(user_model)
        def get(self):
            """Get all users (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Access denied')
            return list(users_db.values())
    
    @ns_pizzas.route('/')
    class PizzasList(Resource):
        @api.marshal_list_with(pizza_model)
        def get(self):
            """Get pizza catalog"""
            return list(pizzas_db.values())
        
        @api.doc(security='Bearer')
        @token_required
        @api.expect(pizza_model)
        @api.marshal_with(pizza_model)
        def post(self):
            """Add new pizza (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Only administrators can add pizzas')
            
            data = request.get_json()
            pizza_id = max(pizzas_db.keys()) + 1 if pizzas_db else 1
            pizza = {
                'id': pizza_id,
                'name': data.get('name'),
                'description': data.get('description'),
                'price': data.get('price'),
                'size': data.get('size', 'Medium'),
                'ingredients': data.get('ingredients', [])
            }
            pizzas_db[pizza_id] = pizza
            return pizza, 201
    
    @ns_pizzas.route('/<int:pizza_id>')
    class Pizza(Resource):
        @api.marshal_with(pizza_model)
        def get(self, pizza_id):
            """Get pizza by ID"""
            pizza = pizzas_db.get(pizza_id)
            if not pizza:
                api.abort(404, 'Pizza not found')
            return pizza
        
        @api.doc(security='Bearer')
        @token_required
        @api.expect(pizza_model)
        @api.marshal_with(pizza_model)
        def put(self, pizza_id):
            """Update pizza by ID (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Only administrators can update pizzas')
            
            pizza = pizzas_db.get(pizza_id)
            if not pizza:
                api.abort(404, 'Pizza not found')
            
            data = request.get_json()
            pizza.update({
                'name': data.get('name', pizza['name']),
                'description': data.get('description', pizza['description']),
                'price': data.get('price', pizza['price']),
                'size': data.get('size', pizza['size']),
                'ingredients': data.get('ingredients', pizza['ingredients'])
            })
            
            return pizza
        
        @api.doc(security='Bearer')
        @token_required
        def delete(self, pizza_id):
            """Delete pizza by ID (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Only administrators can delete pizzas')
            
            if pizza_id not in pizzas_db:
                api.abort(404, 'Pizza not found')
            
            del pizzas_db[pizza_id]
            return {'message': f'Pizza with ID {pizza_id} deleted successfully'}
    
    @ns_orders.route('/')
    class OrdersList(Resource):
        @api.doc(security='Bearer')
        @token_required
        @api.marshal_list_with(order_model)
        def get(self):
            """Get user orders"""
            user_orders = [order for order in orders_db.values() 
                          if order.get('username') == g.current_user]
            return user_orders
        
        @api.doc(security='Bearer')
        @token_required
        def post(self):
            """Create new order"""
            global order_counter
            data = request.get_json()
            pizza_ids = data.get('pizza_ids', [])
            
            if not pizza_ids:
                api.abort(400, 'Order must contain at least one pizza')
            
            ordered_pizzas = []
            total_price = 0
            
            for pid in pizza_ids:
                pizza = pizzas_db.get(pid)
                if pizza:
                    ordered_pizzas.append(pizza)
                    total_price += pizza['price']
            
            order = {
                'id': order_counter,
                'username': g.current_user,
                'user_id': users_db[g.current_user]['id'],
                'pizzas': ordered_pizzas,
                'total_price': total_price,
                'status': 'New',
                'delivery_address': data.get('address', users_db[g.current_user]['address']),
                'created_at': datetime.datetime.utcnow().isoformat()
            }
            
            orders_db[order_counter] = order
            order_counter += 1
            
            return order, 201
    
    @ns_orders.route('/<int:order_id>')
    class Order(Resource):
        @api.doc(security='Bearer')
        @token_required
        @api.marshal_with(order_model)
        def get(self, order_id):
            """Get order by ID"""
            order = orders_db.get(order_id)
            if not order:
                api.abort(404, 'Order not found')
            
            if order['username'] != g.current_user and g.current_user != 'admin':
                api.abort(403, 'Access denied')
            
            return order
        
        @api.doc(security='Bearer')
        @token_required
        def put(self, order_id):
            """Update order status (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Only administrators can update order status')
            
            order = orders_db.get(order_id)
            if not order:
                api.abort(404, 'Order not found')
            
            data = request.get_json()
            new_status = data.get('status')
            
            if new_status:
                order['status'] = new_status
                return order
            
            api.abort(400, 'Status is required')
        
        @api.doc(security='Bearer')
        @token_required
        def delete(self, order_id):
            """Cancel order"""
            order = orders_db.get(order_id)
            if not order:
                api.abort(404, 'Order not found')
            
            if order['username'] != g.current_user and g.current_user != 'admin':
                api.abort(403, 'You can only cancel your own orders')
            
            if order['status'] in ['Preparing', 'On the way', 'Delivered']:
                api.abort(400, 'Cannot cancel order with current status')
            
            del orders_db[order_id]
            return {'message': f'Order {order_id} cancelled'}
    
    @ns_orders.route('/all')
    class AllOrders(Resource):
        @api.doc(security='Bearer')
        @token_required
        @api.marshal_list_with(order_model)
        def get(self):
            """Get all orders (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Access denied')
            return list(orders_db.values())
    
    @ns_orders.route('/stats')
    class OrderStats(Resource):
        @api.doc(security='Bearer')
        @token_required
        def get(self):
            """Order statistics (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Access denied')
            
            total_orders = len(orders_db)
            total_revenue = sum(order.get('total_price', 0) for order in orders_db.values())
            
            status_counts = {}
            for order in orders_db.values():
                status = order.get('status', 'Unknown')
                status_counts[status] = status_counts.get(status, 0) + 1
            
            return {
                'total_orders': total_orders,
                'total_revenue': total_revenue,
                'status_distribution': status_counts,
                'average_order_value': total_revenue / total_orders if total_orders > 0 else 0
            }
    
    @ns_pizzas.route('/popular')
    class PopularPizzas(Resource):
        def get(self):
            """Get top popular pizzas"""
            pizza_counts = {}
            
            for order in orders_db.values():
                for pizza in order.get('pizzas', []):
                    pizza_id = pizza.get('id')
                    if pizza_id:
                        pizza_counts[pizza_id] = pizza_counts.get(pizza_id, 0) + 1
            
            popular_pizzas = []
            for pizza_id, count in sorted(pizza_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                pizza = pizzas_db.get(pizza_id)
                if pizza:
                    popular_pizzas.append({
                        **pizza,
                        'order_count': count
                    })
            
            return popular_pizzas
    
    @ns_pizzas.route('/by-price')
    class PizzasByPrice(Resource):
        def get(self):
            """Pizzas sorted by price"""
            sorted_pizzas = sorted(pizzas_db.values(), key=lambda x: x.get('price', 0))
            return sorted_pizzas
    
    @ns_users.route('/active')
    class ActiveUsers(Resource):
        @api.doc(security='Bearer')
        @token_required
        def get(self):
            """Get active users (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Access denied')
            
            user_order_counts = {}
            for order in orders_db.values():
                username = order.get('username')
                if username:
                    user_order_counts[username] = user_order_counts.get(username, 0) + 1
            
            active_users = []
            for username, order_count in user_order_counts.items():
                user = users_db.get(username)
                if user:
                    active_users.append({
                        'username': username,
                        'email': user.get('email'),
                        'order_count': order_count,
                        'total_spent': sum(order.get('total_price', 0) 
                                         for order in orders_db.values() 
                                         if order.get('username') == username)
                    })
            
            return sorted(active_users, key=lambda x: x['order_count'], reverse=True)
    
    @ns_orders.route('/recent')
    class RecentOrders(Resource):
        @api.doc(security='Bearer')
        @token_required
        def get(self):
            """Recent orders (admin only)"""
            if g.current_user != 'admin':
                api.abort(403, 'Access denied')
            
            recent_orders = sorted(
                orders_db.values(),
                key=lambda x: x.get('created_at', ''),
                reverse=True
            )[:10]
            
            return recent_orders
    
    @ns_health.route('/status')
    class HealthCheck(Resource):
        def get(self):
            """System health check"""
            return {
                'status': 'healthy',
                'message': 'Pizza Delivery API is running!',
                'version': '2.0',
                'database': 'connected',
                'users_count': len(users_db),
                'pizzas_count': len(pizzas_db),
                'orders_count': len(orders_db),
                'timestamp': datetime.datetime.utcnow().isoformat()
            }
    
    @app.route("/hi")
    def hello_world():
        return jsonify({
            'message': 'Hello! Use /api/docs/ to view API documentation',
            'docs_url': '/api/docs/',
            'api_version': '2.0',
            'endpoints': {
                'auth': '/api/v1/auth/',
                'pizzas': '/api/v1/pizzas/',
                'orders': '/api/v1/orders/',
                'health': '/api/v1/health/'
            }
        })


def _init_db(app: Flask) -> None:
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
