from typing import List
from my_project.auth.dao.orders import SaladDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Salad

class SaladService(GeneralService):
    _dao = SaladDAO

    def create(self, salad: Salad) -> None:
        self._dao.create(salad)

    def get_all_salads(self) -> List[Salad]:
        return self._dao.find_all()

    def get_salad_by_id(self, salad_id: int) -> Salad:
        return self._dao.find_by_id(salad_id)

    def update_salad(self, salad_id: int, salad: Salad) -> None:
        self._dao.update(salad_id, salad)

    def delete_salad(self, salad_id: int) -> None:
        self._dao.delete(salad_id)
