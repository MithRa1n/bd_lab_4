# my_project/auth/controller/orders/ToppingController.py
from typing import List
from my_project.auth.dao.orders.ToppingsDAO import ToppingsDAO
from my_project.auth.domain.orders.Toppings import Topping

class ToppingController:
    _dao = ToppingsDAO()

    def find_all(self) -> List[Topping]:
        return self._dao.find_all()

    def create(self, topping: Topping) -> None:
        self._dao.create(topping)

    def find_by_id(self, topping_id: int) -> Topping:
        return self._dao.find_by_id(topping_id)

    def update(self, topping_id: int, topping: Topping) -> None:
        self._dao.update(topping_id, topping)

    def delete(self, topping_id: int) -> None:
        self._dao.delete(topping_id)
