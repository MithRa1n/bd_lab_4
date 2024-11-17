from sqlalchemy import Column, Integer, String
from my_project import db
from typing import Dict, Any
from my_project.auth.domain.i_dto import IDto


class DeliveryStatus(db.Model, IDto):
    __tablename__ = "Delivery_Status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(50), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "status": self.status}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "DeliveryStatus":
        return DeliveryStatus(**dto_dict)
