from typing import List
from my_project.auth.dao.orders import PizzaOrderDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import PizzaOrder

class PizzaOrderService(GeneralService):
    _dao = PizzaOrderDAO

    def create(self, pizza_order: PizzaOrder) -> None:
        self._dao.create(pizza_order)

    def get_all_pizza_orders(self) -> List[PizzaOrder]:
        return self._dao.find_all()

    def get_pizza_order_by_id(self, pizza_order_id: int) -> PizzaOrder:
        return self._dao.find_by_id(pizza_order_id)

    def update_pizza_order(self, pizza_order_id: int, pizza_order: PizzaOrder) -> None:
        self._dao.update(pizza_order_id, pizza_order)

    def delete_pizza_order(self, pizza_order_id: int) -> None:
        self._dao.delete(pizza_order_id)
