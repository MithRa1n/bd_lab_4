# PizzaController.py
from typing import List
from my_project.auth.dao.orders.PizzaDAO import PizzaDAO
from my_project.auth.domain.orders.Pizza import Pizza

class PizzaController:
    _dao = PizzaDAO()

    def find_all(self) -> List[Pizza]:
        """
        Повертає всі піци з бази даних.
        """
        return self._dao.find_all()

    def create(self, pizza: Pizza) -> None:
        """
        Створює новий запис піци.
        """
        self._dao.create(pizza)

    def find_by_id(self, pizza_id: int) -> Pizza:
        """
        Повертає піцу за її ідентифікатором.
        """
        return self._dao.find_by_id(pizza_id)

    def update(self, pizza_id: int, pizza: Pizza) -> None:
        """
        Оновлює запис піци за ідентифікатором.
        """
        self._dao.update(pizza_id, pizza)

    def delete(self, pizza_id: int) -> None:
        """
        Видаляє піцу за її ідентифікатором.
        """
        self._dao.delete(pizza_id)

    def find_by_name(self, name: str) -> List[Pizza]:
        """
        Знаходить піци за назвою.
        """
        return self._dao.find_by_name(name)
