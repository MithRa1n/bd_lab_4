from typing import List
from my_project.auth.dao.orders.DrinksDAO import DrinksDAO
from my_project.auth.domain.orders.Drinks import Drink

class DrinksController:
    _dao = DrinksDAO()

    def find_all(self) -> List[Drink]:
        return self._dao.find_all()

    def create(self, drink: Drink) -> None:
        self._dao.create(drink)

    def find_by_id(self, drink_id: int) -> Drink:
        return self._dao.find_by_id(drink_id)

    def update(self, drink_id: int, drink: Drink) -> None:
        self._dao.update(drink_id, drink)

    def delete(self, drink_id: int) -> None:
        self._dao.delete(drink_id)
