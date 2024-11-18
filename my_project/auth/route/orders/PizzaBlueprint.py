from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pizza_controller
from my_project.auth.domain.orders.Pizza import Pizza

pizza_bp = Blueprint('pizza', __name__, url_prefix='/pizza')

@pizza_bp.get('')
def get_all_pizzas() -> Response:
    pizzas = pizza_controller.find_all()
    pizzas_dto = [pizza.put_into_dto() for pizza in pizzas]
    return make_response(jsonify(pizzas_dto), HTTPStatus.OK)

@pizza_bp.post('')
def create_pizza() -> Response:
    content = request.get_json()
    pizza = Pizza.create_from_dto(content)
    pizza_controller.create(pizza)
    return make_response(jsonify(pizza.put_into_dto()), HTTPStatus.CREATED)

@pizza_bp.get('/<int:pizza_id>')
def get_pizza(pizza_id: int) -> Response:
    pizza = pizza_controller.find_by_id(pizza_id)
    if pizza:
        return make_response(jsonify(pizza.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Pizza not found"}), HTTPStatus.NOT_FOUND)

@pizza_bp.put('/<int:pizza_id>')
def update_pizza(pizza_id: int) -> Response:
    content = request.get_json()
    pizza = Pizza.create_from_dto(content)
    pizza_controller.update(pizza_id, pizza)
    return make_response("Pizza updated", HTTPStatus.OK)

@pizza_bp.delete('/<int:pizza_id>')
def delete_pizza(pizza_id: int) -> Response:
    pizza_controller.delete(pizza_id)
    return make_response("Pizza deleted", HTTPStatus.NO_CONTENT)