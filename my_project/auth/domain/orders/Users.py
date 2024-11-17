from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    U_Name = db.Column(db.String(100), nullable=False)
    U_Surname = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "U_Name": self.U_Name,
            "U_Surname": self.U_Surname,
            "address": self.address,
            "email": self.email,
            "phone_number": self.phone_number,
        }
