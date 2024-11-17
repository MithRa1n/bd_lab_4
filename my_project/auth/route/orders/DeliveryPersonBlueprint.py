from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import delivery_person_controller
from my_project.auth.domain.orders.DeliveryPerson import DeliveryPerson

delivery_person_bp = Blueprint('delivery_person', __name__, url_prefix='/delivery_person')

@delivery_person_bp.get('')
def get_all_delivery_people() -> Response:
    delivery_people = delivery_person_controller.find_all()
    delivery_people_dto = [delivery_person.put_into_dto() for delivery_person in delivery_people]
    return make_response(jsonify(delivery_people_dto), HTTPStatus.OK)

@delivery_person_bp.post('')
def create_delivery_person() -> Response:
    content = request.get_json()
    delivery_person = DeliveryPerson.create_from_dto(content)
    delivery_person_controller.create(delivery_person)
    return make_response(jsonify(delivery_person.put_into_dto()), HTTPStatus.CREATED)


@delivery_person_bp.get('/<int:delivery_person_id>')
def get_delivery_person(delivery_person_id: int) -> Response:
    delivery_person = delivery_person_controller.find_by_id(delivery_person_id)
    if delivery_person:
        return make_response(jsonify(delivery_person.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Delivery person not found"}), HTTPStatus.NOT_FOUND)


@delivery_person_bp.put('/<int:delivery_person_id>')
def update_delivery_person(delivery_person_id: int) -> Response:
    content = request.get_json()
    delivery_person = delivery_person_controller.find_by_id(delivery_person_id)
    if not delivery_person:
        return make_response(jsonify({"error": "Delivery person not found"}), HTTPStatus.NOT_FOUND)

    updated_delivery_person = DeliveryPerson.create_from_dto(content, delivery_person_id)
    delivery_person_controller.update(updated_delivery_person)
    return make_response(jsonify(updated_delivery_person.put_into_dto()), HTTPStatus.OK)


@delivery_person_bp.delete('/<int:delivery_person_id>')
def delete_delivery_person(delivery_person_id: int) -> Response:
    delivery_person = delivery_person_controller.find_by_id(delivery_person_id)
    if not delivery_person:
        return make_response(jsonify({"error": "Delivery person not found"}), HTTPStatus.NOT_FOUND)

    delivery_person_controller.delete(delivery_person_id)
    return make_response(jsonify({"message": "Delivery person deleted successfully"}), HTTPStatus.NO_CONTENT)

