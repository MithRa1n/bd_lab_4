from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import delivery_status_controller
from my_project.auth.domain.orders.DeliveryStatus import DeliveryStatus

delivery_status_bp = Blueprint('delivery_status', __name__, url_prefix='/delivery_status')

@delivery_status_bp.get('')
def get_all_delivery_statuses() -> Response:
    statuses = delivery_status_controller.find_all()
    statuses_dto = [status.put_into_dto() for status in statuses]
    return make_response(jsonify(statuses_dto), HTTPStatus.OK)

@delivery_status_bp.post('')
def create_delivery_status() -> Response:
    content = request.get_json()
    status = DeliveryStatus.create_from_dto(content)
    delivery_status_controller.create(status)
    return make_response(jsonify(status.put_into_dto()), HTTPStatus.CREATED)

@delivery_status_bp.get('/<int:status_id>')
def get_delivery_status(status_id: int) -> Response:
    status = delivery_status_controller.find_by_id(status_id)
    if status:
        return make_response(jsonify(status.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Delivery status not found"}), HTTPStatus.NOT_FOUND)

@delivery_status_bp.put('/<int:status_id>')
def update_delivery_status(status_id: int) -> Response:
    content = request.get_json()
    status = DeliveryStatus.create_from_dto(content)
    delivery_status_controller.update(status_id, status)
    return make_response("Delivery status updated", HTTPStatus.OK)

@delivery_status_bp.delete('/<int:status_id>')
def delete_delivery_status(status_id: int) -> Response:
    delivery_status_controller.delete(status_id)
    return make_response("Delivery status deleted", HTTPStatus.NO_CONTENT)
