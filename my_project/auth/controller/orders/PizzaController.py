# PizzaController.py
from typing import List
from my_project.auth.dao.orders.PizzaDAO import PizzaDAO
from my_project.auth.domain.orders.Pizza import Pizza

class PizzaController:
    _dao = PizzaDAO()

    def find_all(self) -> List[Pizza]:

        return self._dao.find_all()

    def create(self, pizza: Pizza) -> None:

        self._dao.create(pizza)

    def find_by_id(self, pizza_id: int) -> Pizza:

        return self._dao.find_by_id(pizza_id)

    def update(self, pizza_id: int, pizza: Pizza) -> None:

        self._dao.update(pizza_id, pizza)

    def delete(self, pizza_id: int) -> None:

        self._dao.delete(pizza_id)

    def find_by_name(self, name: str) -> List[Pizza]:

        return self._dao.find_by_name(name)