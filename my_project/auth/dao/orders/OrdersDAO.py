from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Orders import Order
from sqlalchemy.orm import joinedload

class OrdersDAO(GeneralDAO):
    _domain_type = Order

    def create(self, order: Order) -> None:
        self._session.add(order)
        self._session.commit()

    def find_all(self) -> List[Order]:
        return self._session.query(Order).options(joinedload(Order.user)).all()

    def find_by_id(self, order_id: int) -> Optional[Order]:
        return self._session.query(Order).filter(Order.id == order_id).first()
