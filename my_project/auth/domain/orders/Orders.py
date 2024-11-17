from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.orders.Users import Users
from my_project.auth.domain.orders.PaymentStatus import PaymentStatus
from my_project.auth.domain.orders.DeliveryStatus import DeliveryStatus


class Order(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    Payment_Statusid = db.Column(db.Integer, db.ForeignKey("Payment_Status.id"), nullable=False)
    Delivery_Statusid = db.Column(db.Integer, db.ForeignKey("Delivery_Status.id"), nullable=False)
    Expected_delivery_time = db.Column(db.DateTime)
    Actual_delivery_time = db.Column(db.DateTime)
    Total_Price = db.Column(db.Numeric(10, 2))
    Created_AT = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("Users", backref="orders")
    payment_status = db.relationship("PaymentStatus", backref="orders")
    delivery_status = db.relationship("DeliveryStatus", backref="orders")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user": self.user.put_into_dto() if self.user else None,
            "payment_status": self.payment_status.put_into_dto() if self.payment_status else None,
            "delivery_status": self.delivery_status.put_into_dto() if self.delivery_status else None,
            "Expected_delivery_time": self.Expected_delivery_time.isoformat() if self.Expected_delivery_time else None,
            "Actual_delivery_time": self.Actual_delivery_time.isoformat() if self.Actual_delivery_time else None,
            "Total_Price": float(self.Total_Price) if self.Total_Price else None,
            "Created_AT": self.Created_AT.isoformat() if self.Created_AT else None,
        }
