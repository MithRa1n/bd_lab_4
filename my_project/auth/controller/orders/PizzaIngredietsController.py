from typing import List
from my_project.auth.dao.orders.PizzaIngredientsDAO import PizzaIngredientsDAO
from my_project.auth.domain.orders.PizzaIngredients import PizzaIngredient

class PizzaIngredientsController:
    _dao = PizzaIngredientsDAO()

    def find_all(self) -> List[PizzaIngredient]:
        return self._dao.find_all()

    def create(self, pizza_ingredient: PizzaIngredient) -> None:
        self._dao.create(pizza_ingredient)

    def find_by_id(self, pizza_id: int, ingredient_id: int) -> PizzaIngredient:
        return self._dao.find_by_id(pizza_id, ingredient_id)

    def update(self, pizza_id: int, ingredient_id: int, pizza_ingredient: PizzaIngredient) -> None:
        self._dao.update(pizza_id, ingredient_id, pizza_ingredient)

    def delete(self, pizza_id: int, ingredient_id: int) -> None:
        self._dao.delete(pizza_id, ingredient_id)
