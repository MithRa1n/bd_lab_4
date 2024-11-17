from typing import List
from my_project.auth.dao.orders import GenderDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Gender

class GenderService(GeneralService):
    _dao = GenderDao

    def create(self, gender: Gender) -> None:
        self._dao.create(gender)

    def get_all_genders(self) -> List[Gender]:
        return self._dao.find_all()

    def get_gender_by_id(self, gender_id: int) -> Gender:
        return self._dao.find_by_id(gender_id)

    def update_gender(self, gender_id: int, gender: Gender) -> None:
        self._dao.update(gender_id, gender)

    def delete_gender(self, gender_id: int) -> None:
        self._dao.delete(gender_id)