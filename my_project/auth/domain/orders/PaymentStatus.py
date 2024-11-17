from __future__ import annotations
from typing import Dict, Any
from my_project import db


class PaymentStatus(db.Model):
    __tablename__ = "Payment_Status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(50), nullable=False)


    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "status": self.status}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PaymentStatus:
        return PaymentStatus(**dto_dict)
