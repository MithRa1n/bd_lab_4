from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Ingredients import Ingredient

class IngredientsDAO(GeneralDAO):
    _domain_type = Ingredient

    def create(self, ingredient: Ingredient) -> None:
        self._session.add(ingredient)
        self._session.commit()

    def find_all(self) -> List[Ingredient]:
        return self._session.query(Ingredient).all()

    def find_by_id(self, ingredient_id: int) -> Optional[Ingredient]:
        return self._session.query(Ingredient).filter(Ingredient.ingredient_id == ingredient_id).first()