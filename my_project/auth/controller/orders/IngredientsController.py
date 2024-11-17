from typing import List
from my_project.auth.dao.orders.IngredientsDAO import IngredientsDAO
from my_project.auth.domain.orders.Ingredients import Ingredient

class IngredientsController:
    _dao = IngredientsDAO()

    def find_all(self) -> List[Ingredient]:
        return self._dao.find_all()

    def create(self, ingredient: Ingredient) -> None:
        self._dao.create(ingredient)

    def find_by_id(self, ingredient_id: int) -> Ingredient:
        return self._dao.find_by_id(ingredient_id)

    def update(self, ingredient_id: int, ingredient: Ingredient) -> None:
        self._dao.update(ingredient_id, ingredient)

    def delete(self, ingredient_id: int) -> None:
        self._dao.delete(ingredient_id)
