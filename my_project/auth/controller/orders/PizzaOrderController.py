from typing import List
from my_project.auth.dao.orders.PizzaOrderDAO import PizzaOrderDAO
from my_project.auth.domain.orders.PizzaOrder import PizzaOrder

class PizzaOrderController:
    _dao = PizzaOrderDAO()

    def find_all(self) -> List[PizzaOrder]:
        return self._dao.find_all()

    def create(self, pizza_order: PizzaOrder) -> None:
        self._dao.create(pizza_order)

    def find_by_id(self, pizza_order_id: int) -> PizzaOrder:
        return self._dao.find_by_id(pizza_order_id)

    def update(self, pizza_order_id: int, pizza_order: PizzaOrder) -> None:
        self._dao.update(pizza_order_id, pizza_order)

    def delete(self, pizza_order_id: int) -> None:
        self._dao.delete(pizza_order_id)
