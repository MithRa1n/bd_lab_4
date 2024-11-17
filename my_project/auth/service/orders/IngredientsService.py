from typing import List
from my_project.auth.dao.orders import IngredientsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Ingredients

class IngredientsService(GeneralService):
    _dao = IngredientsDAO

    def create(self, ingredients: Ingredients) -> None:
        self._dao.create(ingredients)

    def get_all_ingredients(self) -> List[Ingredients]:
        return self._dao.find_all()

    def get_ingredients_by_id(self, ingredients_id: int) -> Ingredients:
        return self._dao.find_by_id(ingredients_id)

    def update_ingredients(self, ingredients_id: int, ingredients: Ingredients) -> None:
        self._dao.update(ingredients_id, ingredients)

    def delete_ingredients(self, ingredients_id: int) -> None:
        self._dao.delete(ingredients_id)
