from typing import List
from my_project.auth.dao.orders import ToppingsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Toppings

class ToppingsService(GeneralService):
    _dao = ToppingsDAO

    def create(self, toppings: Toppings) -> None:
        self._dao.create(toppings)

    def get_all_toppings(self) -> List[Toppings]:
        return self._dao.find_all()

    def get_toppings_by_id(self, toppings_id: int) -> Toppings:
        return self._dao.find_by_id(toppings_id)

    def update_toppings(self, toppings_id: int, toppings: Toppings) -> None:
        self._dao.update(toppings_id, toppings)

    def delete_toppings(self, toppings_id: int) -> None:
        self._dao.delete(toppings_id)
