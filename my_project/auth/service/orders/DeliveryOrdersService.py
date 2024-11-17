from typing import List
from my_project.auth.dao.orders import DeliveryOrdersDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import DeliveryOrders

class DeliveryOrdersService(GeneralService):
    _dao = DeliveryOrdersDAO

    def create(self, delivery_order: DeliveryOrders) -> None:
        self._dao.create(delivery_order)

    def get_all_delivery_orders(self) -> List[DeliveryOrders]:
        return self._dao.find_all()

    def get_delivery_order_by_id(self, delivery_order_id: int) -> DeliveryOrders:
        return self._dao.find_by_id(delivery_order_id)

    def update_delivery_order(self, delivery_order_id: int, delivery_order: DeliveryOrders) -> None:
        self._dao.update(delivery_order_id, delivery_order)

    def delete_delivery_order(self, delivery_order_id: int) -> None:
        self._dao.delete(delivery_order_id)
