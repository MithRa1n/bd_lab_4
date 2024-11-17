from typing import List
from my_project.auth.dao.orders.OrdersDAO import OrdersDAO
from my_project.auth.domain.orders.Orders import Order

class OrdersController:
    _dao = OrdersDAO()

    def find_all(self) -> List[Order]:
        return self._dao.find_all()

    def create(self, order: Order) -> None:
        self._dao.create(order)

    def find_by_id(self, order_id: int) -> Order:
        return self._dao.find_by_id(order_id)

    def update(self, order_id: int, order: Order) -> None:
        self._dao.update(order_id, order)

    def delete(self, order_id: int) -> None:
        self._dao.delete(order_id)
