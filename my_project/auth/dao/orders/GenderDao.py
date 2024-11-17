from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Gender import Gender

class GenderDAO(GeneralDAO):
    _domain_type = Gender

    def create(self, gender: Gender) -> None:
        self._session.add(gender)
        self._session.commit()

    def find_all(self) -> List[Gender]:
        return self._session.query(Gender).all()

    def find_by_id(self, gender_id: int) -> Optional[Gender]:
        return self._session.query(Gender).filter(Gender.id == gender_id).first()
