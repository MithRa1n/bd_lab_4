from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import drinks_controller
from my_project.auth.domain.orders.Drinks import Drink

drinks_bp = Blueprint('drinks', __name__, url_prefix='/drinks')

@drinks_bp.get('')
def get_all_drinks() -> Response:
    drinks = drinks_controller.find_all()
    drinks_dto = [drink.put_into_dto() for drink in drinks]
    return make_response(jsonify(drinks_dto), HTTPStatus.OK)

@drinks_bp.post('')
def create_drink() -> Response:
    content = request.get_json()
    drink = Drink.create_from_dto(content)
    drinks_controller.create(drink)
    return make_response(jsonify(drink.put_into_dto()), HTTPStatus.CREATED)

@drinks_bp.get('/<int:drink_id>')
def get_drink(drink_id: int) -> Response:
    drink = drinks_controller.find_by_id(drink_id)
    if drink:
        return make_response(jsonify(drink.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Drink not found"}), HTTPStatus.NOT_FOUND)

@drinks_bp.put('/<int:drink_id>')
def update_drink(drink_id: int) -> Response:
    content = request.get_json()
    drink = Drink.create_from_dto(content)
    drinks_controller.update(drink_id, drink)
    return make_response("Drink updated", HTTPStatus.OK)

@drinks_bp.delete('/<int:drink_id>')
def delete_drink(drink_id: int) -> Response:
    drinks_controller.delete(drink_id)
    return make_response("Drink deleted", HTTPStatus.NO_CONTENT)
