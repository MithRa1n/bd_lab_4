from __future__ import annotations
from typing import Dict, Any
from my_project import db


class PizzaOrder(db.Model):
    __tablename__ = "Pizza_Order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey("Pizza.id"), nullable=False)
    toppings_id = db.Column(db.Integer, db.ForeignKey("Toppings.topping_id"))
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "pizza_id": self.pizza_id,
            "toppings_id": self.toppings_id,
            "price": float(self.price),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PizzaOrder:
        return PizzaOrder(**dto_dict)
