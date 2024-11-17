from typing import Dict, Any
from sqlalchemy import Column, Integer, String
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Gender(db.Model, IDto):
    __tablename__ = "Gender"
    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(String(50), nullable=False)


    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "gender": self.gender}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Gender":
        return Gender(**dto_dict)
