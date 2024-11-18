from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Ingredient(db.Model):
    __tablename__ = "Ingredients"

    ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    pizzas = db.relationship(
        "Pizza",
        secondary="Pizza_Ingredients",
        back_populates="ingredients"
    )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "ingredient_id": self.ingredient_id,
            "name": self.name,
            "quantity": self.quantity,        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ingredient:
        return Ingredient(**dto_dict)