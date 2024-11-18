from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.PizzaIngredietsController import PizzaIngredientsController
from my_project.auth.domain.orders.PizzaIngredients import PizzaIngredient

pizza_ingredients_bp = Blueprint('pizza_ingredients', __name__, url_prefix='/pizza_ingredients')

@pizza_ingredients_bp.get('')
def get_all_pizza_ingredients() -> Response:
    pizza_ingredients = PizzaIngredientsController.find_all()
    pizza_ingredients_dto = [pizza_ingredient.put_into_dto() for pizza_ingredient in pizza_ingredients]
    return make_response(jsonify(pizza_ingredients_dto), HTTPStatus.OK)

@pizza_ingredients_bp.post('')
def create_pizza_ingredient() -> Response:
    content = request.get_json()
    pizza_ingredient = PizzaIngredient.create_from_dto(content)
    PizzaIngredientsController.create(pizza_ingredient)
    return make_response(jsonify(pizza_ingredient.put_into_dto()), HTTPStatus.CREATED)

@pizza_ingredients_bp.get('/<int:pizza_ingredient_id>')
def get_pizza_ingredient(pizza_ingredient_id: int) -> Response:
    pizza_ingredient = PizzaIngredientsController.find_by_id(pizza_ingredient_id)
    if pizza_ingredient:
        return make_response(jsonify(pizza_ingredient.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Pizza ingredient not found"}), HTTPStatus.NOT_FOUND)

@pizza_ingredients_bp.put('/<int:pizza_ingredient_id>')
def update_pizza_ingredient(pizza_ingredient_id: int) -> Response:
    content = request.get_json()
    pizza_ingredient = PizzaIngredient.create_from_dto(content)
    PizzaIngredientsController.update(pizza_ingredient_id, pizza_ingredient)
    return make_response("Pizza ingredient updated", HTTPStatus.OK)

@pizza_ingredients_bp.delete('/<int:pizza_ingredient_id>')
def delete_pizza_ingredient(pizza_ingredient_id: int) -> Response:
    PizzaIngredientsController.delete(pizza_ingredient_id)
    return make_response("Pizza ingredient deleted", HTTPStatus.NO_CONTENT)

@pizza_ingredients_bp.route('/pizza-ingredients', methods=['GET'])
def get_pizza_ingredients_with_details():
    """
    Отримує всі записи PizzaIngredients з деталями про піци та інгредієнти.
    """
    controller = PizzaIngredientsController()
    data = controller.find_all_with_details()  # Метод для отримання розширених даних
    return jsonify(data)