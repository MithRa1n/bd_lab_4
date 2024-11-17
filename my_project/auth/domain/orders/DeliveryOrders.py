from __future__ import annotations
from typing import Dict, Any
from my_project import db


class DeliveryOrder(db.Model):
    __tablename__ = "Delivery_Orders"

    DeliveryID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderID = db.Column(db.Integer, db.ForeignKey("Orders.id"), nullable=False)
    DeliveryPersonID = db.Column(db.Integer, db.ForeignKey("Delivery_Person.id"), nullable=False)
    EstimatedDeliveryTime = db.Column(db.DateTime)
    ActualDeliveryTime = db.Column(db.DateTime)
    CreatedAt = db.Column(db.DateTime, default=db.func.now())
    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "DeliveryID": self.DeliveryID,
            "OrderID": self.OrderID,
            "DeliveryPersonID": self.DeliveryPersonID,
            "EstimatedDeliveryTime": self.EstimatedDeliveryTime,
            "ActualDeliveryTime": self.ActualDeliveryTime,
            "CreatedAt": self.CreatedAt,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DeliveryOrder:
        return DeliveryOrder(**dto_dict)
