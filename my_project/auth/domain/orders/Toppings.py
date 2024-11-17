from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Topping(db.Model):
    __tablename__ = "Toppings"

    topping_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topping_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "topping_id": self.topping_id,
            "topping_name": self.topping_name,
            "quantity": self.quantity,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Topping:
        return Topping(**dto_dict)
