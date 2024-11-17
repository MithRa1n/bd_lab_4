from typing import List
from my_project.auth.dao.orders import DrinksDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Drinks

class DrinksService(GeneralService):
    _dao = DrinksDAO

    def create(self, drink: Drinks) -> None:
        self._dao.create(drink)

    def get_all_drinks(self) -> List[Drinks]:
        return self._dao.find_all()

    def get_drink_by_id(self, drink_id: int) -> Drinks:
        return self._dao.find_by_id(drink_id)

    def update_drink(self, drink_id: int, drink: Drinks) -> None:
        self._dao.update(drink_id, drink)

    def delete_drink(self, drink_id: int) -> None:
        self._dao.delete(drink_id)
