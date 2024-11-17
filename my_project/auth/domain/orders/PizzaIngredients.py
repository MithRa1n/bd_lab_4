from __future__ import annotations
from typing import Dict, Any
from my_project import db


class PizzaIngredient(db.Model):
    __tablename__ = "Pizza_Ingredients"

    pizza_id = db.Column(db.Integer, db.ForeignKey("Pizza.id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("Ingredients.ingredient_id"), primary_key=True)



    def put_into_dto(self) -> Dict[str, Any]:
        return {"pizza_id": self.pizza_id, "ingredient_id": self.ingredient_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PizzaIngredient:
        return PizzaIngredient(**dto_dict)
