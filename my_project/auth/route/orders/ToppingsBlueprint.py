from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.ToppingController import ToppingController
from my_project.auth.domain.orders.Toppings import Topping

toppings_bp = Blueprint('toppings', __name__, url_prefix='/toppings')

@toppings_bp.get('')
def get_all_toppings() -> Response:
    toppings = ToppingController.find_all()
    toppings_dto = [topping.put_into_dto() for topping in toppings]
    return make_response(jsonify(toppings_dto), HTTPStatus.OK)

@toppings_bp.post('')
def create_topping() -> Response:
    content = request.get_json()
    topping = Topping.create_from_dto(content)
    ToppingController.create(topping)
    return make_response(jsonify(topping.put_into_dto()), HTTPStatus.CREATED)

@toppings_bp.get('/<int:topping_id>')
def get_topping(topping_id: int) -> Response:
    topping = ToppingController.find_by_id(topping_id)
    if topping:
        return make_response(jsonify(topping.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Topping not found"}), HTTPStatus.NOT_FOUND)

@toppings_bp.put('/<int:topping_id>')
def update_topping(topping_id: int) -> Response:
    content = request.get_json()
    topping = Topping.create_from_dto(content)
    ToppingController.update(topping_id, topping)
    return make_response("Topping updated", HTTPStatus.OK)

@toppings_bp.delete('/<int:topping_id>')
def delete_topping(topping_id: int) -> Response:
    ToppingController.delete(topping_id)
    return make_response("Topping deleted", HTTPStatus.NO_CONTENT)
