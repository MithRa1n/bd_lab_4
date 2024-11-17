from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Pizza(db.Model):
    __tablename__ = "Pizza"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    ingredients = db.relationship(
        "Ingredient",
        secondary="Pizza_Ingredients",
        back_populates="pizzas"
    )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "ingredients": [ingredient.put_into_dto() for ingredient in self.ingredients]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Pizza:
        return Pizza(**dto_dict)
