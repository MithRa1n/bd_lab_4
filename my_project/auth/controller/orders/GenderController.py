from typing import List
from my_project.auth.dao.orders.GenderDao import GenderDAO
from my_project.auth.domain.orders.Gender import Gender

class GenderController:
    _dao = GenderDAO()

    def find_all(self) -> List[Gender]:
        return self._dao.find_all()

    def create(self, gender: Gender) -> None:
        self._dao.create(gender)

    def find_by_id(self, gender_id: int) -> Gender:
        return self._dao.find_by_id(gender_id)

    def update(self, gender_id: int, gender: Gender) -> None:
        self._dao.update(gender_id, gender)

    def delete(self, gender_id: int) -> None:
        self._dao.delete(gender_id)
