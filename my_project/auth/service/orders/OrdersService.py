from typing import List
from my_project.auth.dao.orders import OrdersDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Orders

class OrdersService(GeneralService):
    _dao = OrdersDAO

    def create(self, order: Orders) -> None:
        self._dao.create(order)

    def get_all_orders(self) -> List[Orders]:
        return self._dao.find_all()

    def get_order_by_id(self, order_id: int) -> Orders:
        return self._dao.find_by_id(order_id)

    def update_order(self, order_id: int, order: Orders) -> None:
        self._dao.update(order_id, order)

    def delete_order(self, order_id: int) -> None:
        self._dao.delete(order_id)
