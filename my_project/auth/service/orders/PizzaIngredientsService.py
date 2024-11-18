from typing import List
from my_project.auth.dao.orders import PizzaIngredientsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import PizzaIngredients

class PizzaIngredientsService(GeneralService):
    _dao = PizzaIngredientsDAO

    def create(self, pizza_ingredient: PizzaIngredients) -> None:
        self._dao.create(pizza_ingredient)

    def get_all_pizza_ingredients(self) -> List[PizzaIngredients]:
        return self._dao.find_all()

    def get_pizza_ingredient_by_pizza_id(self, pizza_id: int) -> List[PizzaIngredients]:
        return self._dao.find_by_pizza_id(pizza_id)

    def get_pizza_ingredient_by_ingredient_id(self, ingredient_id: int) -> List[PizzaIngredients]:
        return self._dao.find_by_ingredient_id(ingredient_id)

    def delete_pizza_ingredient(self, pizza_id: int, ingredient_id: int) -> None:
        self._dao.delete(pizza_id, ingredient_id)