

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity.
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each specific entity
    from .orders.GenderBlueprint import gender_bp
    from .orders.PizzaBlueprint import pizza_bp
    from .orders.SaladBlueprint import salad_bp
    from .orders.UsersBlueprint import users_bp
    from .orders.DrinksBlueprint import drinks_bp
    from .orders.DeliveryPersonBlueprint import delivery_person_bp
    from .orders.DeliveryStatusBlueprint import delivery_status_bp
    from .orders.PaymentStatusBlueprint import payment_status_bp
    from .orders.ToppingsBlueprint import toppings_bp
    from .orders.PizzaIngredientsBlueprint import pizza_ingredients_bp
    from .orders.IngredientsBlueprint import ingredients_bp
    from .orders.OrdersBlueprint import orders_bp
    from .orders.PizzaOrderBlueprint import pizza_order_bp
    from .orders.DeliveryStatusBlueprint import delivery_status_bp

    # Register each blueprint with the app
    app.register_blueprint(gender_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(salad_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(drinks_bp)
    app.register_blueprint(delivery_person_bp)
    app.register_blueprint(delivery_status_bp)
    app.register_blueprint(payment_status_bp)
    app.register_blueprint(toppings_bp)
    app.register_blueprint(pizza_ingredients_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(pizza_order_bp)
