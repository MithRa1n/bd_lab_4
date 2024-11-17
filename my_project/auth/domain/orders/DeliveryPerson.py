from __future__ import annotations
from typing import Dict, Any
from my_project import db


class DeliveryPerson(db.Model):
    __tablename__ = "Delivery_Person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Surname = db.Column(db.String(255), nullable=False)
    Gender = db.Column(db.Integer, db.ForeignKey("Gender.id"))
    PhoneNumber = db.Column(db.String(15))
    CurrentLocation = db.Column(db.String(255))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "Name": self.Name,
            "Surname": self.Surname,
            "Gender": self.Gender,
            "PhoneNumber": self.PhoneNumber,
            "CurrentLocation": self.CurrentLocation,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DeliveryPerson:
        return DeliveryPerson(**dto_dict)