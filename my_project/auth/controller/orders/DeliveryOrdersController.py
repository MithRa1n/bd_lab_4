from typing import List
from my_project.auth.dao.orders.DeliveryOrdersDAO import DeliveryOrdersDAO
from my_project.auth.domain.orders.DeliveryOrders import DeliveryOrder

class DeliveryOrdersController:
    _dao = DeliveryOrdersDAO()

    def find_all(self) -> List[DeliveryOrder]:
        return self._dao.find_all()

    def create(self, delivery_order: DeliveryOrder) -> None:
        self._dao.create(delivery_order)

    def find_by_id(self, delivery_order_id: int) -> DeliveryOrder:
        return self._dao.find_by_id(delivery_order_id)

    def update(self, delivery_order_id: int, delivery_order: DeliveryOrder) -> None:
        self._dao.update(delivery_order_id, delivery_order)

    def delete(self, delivery_order_id: int) -> None:
        self._dao.delete(delivery_order_id)
