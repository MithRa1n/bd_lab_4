from typing import List
from my_project.auth.dao.orders.SaladDAO import SaladDAO
from my_project.auth.domain.orders.Salad import Salad

class SaladController:
    _dao = SaladDAO()

    def find_all(self) -> List[Salad]:
        return self._dao.find_all()

    def create(self, salad: Salad) -> None:
        self._dao.create(salad)

    def find_by_id(self, salad_id: int) -> Salad:
        return self._dao.find_by_id(salad_id)

    def update(self, salad_id: int, salad: Salad) -> None:
        self._dao.update(salad_id, salad)

    def delete(self, salad_id: int) -> None:
        self._dao.delete(salad_id)
