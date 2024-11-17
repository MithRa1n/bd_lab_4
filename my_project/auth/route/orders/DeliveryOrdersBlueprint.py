from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import delivery_orders_controller
from my_project.auth.domain.orders.DeliveryOrders import DeliveryOrder

delivery_orders_bp = Blueprint('delivery_orders', __name__, url_prefix='/delivery_orders')

@delivery_orders_bp.get('')
def get_all_delivery_orders() -> Response:
    delivery_orders = delivery_orders_controller.find_all()
    delivery_orders_dto = [delivery_order.put_into_dto() for delivery_order in delivery_orders]
    return make_response(jsonify(delivery_orders_dto), HTTPStatus.OK)

@delivery_orders_bp.post('')
def create_delivery_order() -> Response:
    content = request.get_json()
    delivery_order = DeliveryOrder.create_from_dto(content)
    delivery_orders_controller.create(delivery_order)
    return make_response(jsonify(delivery_order.put_into_dto()), HTTPStatus.CREATED)

@delivery_orders_bp.get('/<int:delivery_order_id>')
def get_delivery_order(delivery_order_id: int) -> Response:
    delivery_order = delivery_orders_controller.find_by_id(delivery_order_id)
    if delivery_order:
        return make_response(jsonify(delivery_order.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Delivery order not found"}), HTTPStatus.NOT_FOUND)

@delivery_orders_bp.put('/<int:delivery_order_id>')
def update_delivery_order(delivery_order_id: int) -> Response:
    content = request.get_json()
    delivery_order = delivery_orders_controller.find_by_id(delivery_order_id)
    if not delivery_order:
        return make_response(jsonify({"error": "Delivery order not found"}), HTTPStatus.NOT_FOUND)

    updated_delivery_order = DeliveryOrder.create_from_dto(content)
    updated_delivery_order.DeliveryID = delivery_order_id
    delivery_orders_controller.update(updated_delivery_order)
    return make_response(jsonify(updated_delivery_order.put_into_dto()), HTTPStatus.OK)

@delivery_orders_bp.delete('/<int:delivery_order_id>')
def delete_delivery_order(delivery_order_id: int) -> Response:
    delivery_order = delivery_orders_controller.find_by_id(delivery_order_id)
    if not delivery_order:
        return make_response(jsonify({"error": "Delivery order not found"}), HTTPStatus.NOT_FOUND)

    delivery_orders_controller.delete(delivery_order_id)
    return make_response(jsonify({"message": "Delivery order deleted successfully"}), HTTPStatus.NO_CONTENT)
