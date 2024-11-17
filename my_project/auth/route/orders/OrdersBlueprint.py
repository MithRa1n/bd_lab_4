from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import orders_controller
from my_project.auth.domain.orders.Orders import Order

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.get('')
def get_all_orders() -> Response:
    orders = orders_controller.find_all()
    orders_dto = [order.put_into_dto() for order in orders]
    return make_response(jsonify(orders_dto), HTTPStatus.OK)

@orders_bp.post('')
def create_order() -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    orders_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)

@orders_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    order = orders_controller.find_by_id(order_id)
    if order:
        return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Order not found"}), HTTPStatus.NOT_FOUND)

@orders_bp.put('/<int:order_id>')
def update_order(order_id: int) -> Response:
    content = request.get_json()
    order = orders_controller.find_by_id(order_id)
    if not order:
        return make_response(jsonify({"error": "Order not found"}), HTTPStatus.NOT_FOUND)

    updated_order = Order.create_from_dto(content)
    updated_order.id = order_id
    orders_controller.update(updated_order)
    return make_response(jsonify(updated_order.put_into_dto()), HTTPStatus.OK)

@orders_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    order = orders_controller.find_by_id(order_id)
    if not order:
        return make_response(jsonify({"error": "Order not found"}), HTTPStatus.NOT_FOUND)

    orders_controller.delete(order_id)
    return make_response(jsonify({"message": "Order deleted successfully"}), HTTPStatus.NO_CONTENT)
