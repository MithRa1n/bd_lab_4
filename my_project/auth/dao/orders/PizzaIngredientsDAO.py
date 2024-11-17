from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PizzaIngredients import PizzaIngredient

class PizzaIngredientsDAO(GeneralDAO):
    _domain_type = PizzaIngredient

    def create(self, pizza_ingredient: PizzaIngredient) -> None:
        self._session.add(pizza_ingredient)
        self._session.commit()

    def find_all(self) -> List[PizzaIngredient]:
        return self._session.query(PizzaIngredient).all()

    def find_by_pizza_id(self, pizza_id: int) -> List[PizzaIngredient]:
        return self._session.query(PizzaIngredient).filter(PizzaIngredient.pizza_id == pizza_id).all()
