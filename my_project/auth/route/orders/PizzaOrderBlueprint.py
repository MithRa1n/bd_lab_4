from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pizza_order_controller
from my_project.auth.domain.orders.PizzaOrder import PizzaOrder

pizza_order_bp = Blueprint('pizza_order', __name__, url_prefix='/pizza_order')

@pizza_order_bp.get('')
def get_all_pizza_orders() -> Response:
    pizza_orders = pizza_order_controller.find_all()
    pizza_orders_dto = [pizza_order.put_into_dto() for pizza_order in pizza_orders]
    return make_response(jsonify(pizza_orders_dto), HTTPStatus.OK)

@pizza_order_bp.post('')
def create_pizza_order() -> Response:
    content = request.get_json()
    pizza_order = PizzaOrder.create_from_dto(content)
    pizza_order_controller.create(pizza_order)
    return make_response(jsonify(pizza_order.put_into_dto()), HTTPStatus.CREATED)

@pizza_order_bp.get('/<int:pizza_order_id>')
def get_pizza_order(pizza_order_id: int) -> Response:
    pizza_order = pizza_order_controller.find_by_id(pizza_order_id)
    if pizza_order:
        return make_response(jsonify(pizza_order.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Pizza order not found"}), HTTPStatus.NOT_FOUND)

@pizza_order_bp.put('/<int:pizza_order_id>')
def update_pizza_order(pizza_order_id: int) -> Response:
    content = request.get_json()
    pizza_order = pizza_order_controller.find_by_id(pizza_order_id)
    if not pizza_order:
        return make_response(jsonify({"error": "Pizza order not found"}), HTTPStatus.NOT_FOUND)

    updated_pizza_order = PizzaOrder.create_from_dto(content)
    updated_pizza_order.id = pizza_order_id
    pizza_order_controller.update(updated_pizza_order)
    return make_response(jsonify(updated_pizza_order.put_into_dto()), HTTPStatus.OK)

@pizza_order_bp.delete('/<int:pizza_order_id>')
def delete_pizza_order(pizza_order_id: int) -> Response:
    pizza_order = pizza_order_controller.find_by_id(pizza_order_id)
    if not pizza_order:
        return make_response(jsonify({"error": "Pizza order not found"}), HTTPStatus.NOT_FOUND)

    pizza_order_controller.delete(pizza_order_id)
    return make_response(jsonify({"message": "Pizza order deleted successfully"}), HTTPStatus.NO_CONTENT)
