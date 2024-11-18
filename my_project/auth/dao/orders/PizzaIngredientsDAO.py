from typing import List, Optional, Dict

from sqlalchemy.orm import joinedload

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

    def find_all_with_details(self) -> List[Dict]:
        """
        Повертає список записів PizzaIngredients з розгорнутими даними про піцу та інгредієнти.
        """
        query = (
            self._session.query(PizzaIngredient)
            .options(joinedload(PizzaIngredient.pizza), joinedload(PizzaIngredient.ingredient))
        )
        result = []

        for record in query.all():
            result.append({
                "pizza_ingredient": {
                    "pizza_id": record.pizza_id,
                    "ingredient_id": record.ingredient_id
                },
                "pizza": {
                    "id": record.pizza.id,
                    "name": record.pizza.name,
                    "quantity": record.pizza.quantity
                },
                "ingredient": {
                    "ingredient_id": record.ingredient.ingredient_id,
                    "name": record.ingredient.name,
                    "quantity": record.ingredient.quantity
                }
            })

        return result