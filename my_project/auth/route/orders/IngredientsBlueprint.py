from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import ingredients_controller
from my_project.auth.domain.orders.Ingredients import Ingredient

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')

@ingredients_bp.get('')
def get_all_ingredients() -> Response:
    ingredients = ingredients_controller.find_all()
    ingredients_dto = [ingredient.put_into_dto() for ingredient in ingredients]
    return make_response(jsonify(ingredients_dto), HTTPStatus.OK)

@ingredients_bp.post('')
def create_ingredient() -> Response:
    content = request.get_json()
    ingredient = Ingredient.create_from_dto(content)
    ingredients_controller.create(ingredient)
    return make_response(jsonify(ingredient.put_into_dto()), HTTPStatus.CREATED)

@ingredients_bp.get('/<int:ingredient_id>')
def get_ingredient(ingredient_id: int) -> Response:
    ingredient = ingredients_controller.find_by_id(ingredient_id)
    if ingredient:
        return make_response(jsonify(ingredient.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Ingredient not found"}), HTTPStatus.NOT_FOUND)

@ingredients_bp.put('/<int:ingredient_id>')
def update_ingredient(ingredient_id: int) -> Response:
    content = request.get_json()
    ingredient = Ingredient.create_from_dto(content)
    ingredients_controller.update(ingredient_id, ingredient)
    return make_response("Ingredient updated", HTTPStatus.OK)

@ingredients_bp.delete('/<int:ingredient_id>')
def delete_ingredient(ingredient_id: int) -> Response:
    ingredients_controller.delete(ingredient_id)
    return make_response("Ingredient deleted", HTTPStatus.NO_CONTENT)
