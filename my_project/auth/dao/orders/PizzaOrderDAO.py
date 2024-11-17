from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PizzaOrder import PizzaOrder

class PizzaOrderDAO(GeneralDAO):
    _domain_type = PizzaOrder

    def create(self, pizza_order: PizzaOrder) -> None:
        self._session.add(pizza_order)
        self._session.commit()

    def find_all(self) -> List[PizzaOrder]:
        return self._session.query(PizzaOrder).all()

    def find_by_id(self, pizza_order_id: int) -> Optional[PizzaOrder]:
        return self._session.query(PizzaOrder).filter(PizzaOrder.id == pizza_order_id).first()
