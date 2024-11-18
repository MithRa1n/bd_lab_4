from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.orders.Pizza import Pizza
from my_project.auth.domain.orders.Ingredients import Ingredient


class PizzaIngredient(db.Model):
    __tablename__ = "Pizza_Ingredients"

    pizza_id = db.Column(db.Integer, db.ForeignKey("Pizza.id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("Ingredients.ingredient_id"), primary_key=True)

    pizza = db.relationship("Pizza", backref="pizza_ingredients", lazy="joined")
    ingredient = db.relationship("Ingredient", backref="ingredient_pizzas", lazy="joined")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "pizza_id": self.pizza_id,
            "ingredient_id": self.ingredient_id,
            "pizza": self.pizza.put_into_dto(),
            "ingredient": self.ingredient.put_into_dto()
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PizzaIngredient:
        return PizzaIngredient(**dto_dict)
