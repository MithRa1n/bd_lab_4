from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import payment_status_controller
from my_project.auth.domain.orders.PaymentStatus import PaymentStatus

payment_status_bp = Blueprint('payment_status', __name__, url_prefix='/payment_status')

@payment_status_bp.get('')
def get_all_payment_statuses() -> Response:
    statuses = payment_status_controller.find_all()
    statuses_dto = [status.put_into_dto() for status in statuses]
    return make_response(jsonify(statuses_dto), HTTPStatus.OK)

@payment_status_bp.post('')
def create_payment_status() -> Response:
    content = request.get_json()
    status = PaymentStatus.create_from_dto(content)
    payment_status_controller.create(status)
    return make_response(jsonify(status.put_into_dto()), HTTPStatus.CREATED)

@payment_status_bp.get('/<int:status_id>')
def get_payment_status(status_id: int) -> Response:
    status = payment_status_controller.find_by_id(status_id)
    if status:
        return make_response(jsonify(status.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Payment status not found"}), HTTPStatus.NOT_FOUND)

@payment_status_bp.put('/<int:status_id>')
def update_payment_status(status_id: int) -> Response:
    content = request.get_json()
    status = PaymentStatus.create_from_dto(content)
    payment_status_controller.update(status_id, status)
    return make_response("Payment status updated", HTTPStatus.OK)

@payment_status_bp.delete('/<int:status_id>')
def delete_payment_status(status_id: int) -> Response:
    payment_status_controller.delete(status_id)
    return make_response("Payment status deleted", HTTPStatus.NO_CONTENT)
