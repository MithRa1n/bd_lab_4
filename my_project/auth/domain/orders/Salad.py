from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Salad(db.Model):
    __tablename__ = "Salad"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "price": float(self.price)}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Salad:
        return Salad(**dto_dict)
