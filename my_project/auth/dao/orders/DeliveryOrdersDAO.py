from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.DeliveryOrders import DeliveryOrder

class DeliveryOrdersDAO(GeneralDAO):
    _domain_type = DeliveryOrder

    def create(self, delivery_order: DeliveryOrder) -> None:
        self._session.add(delivery_order)
        self._session.commit()

    def find_all(self) -> List[DeliveryOrder]:
        return self._session.query(DeliveryOrder).all()

    def find_by_id(self, delivery_order_id: int) -> Optional[DeliveryOrder]:
        return self._session.query(DeliveryOrder).filter(DeliveryOrder.id == delivery_order_id).first()
