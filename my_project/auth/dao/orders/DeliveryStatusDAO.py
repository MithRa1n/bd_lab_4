from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.DeliveryStatus import DeliveryStatus

class DeliveryStatusDAO(GeneralDAO):
    _domain_type = DeliveryStatus

    def create(self, status: DeliveryStatus) -> None:
        self._session.add(status)
        self._session.commit()

    def find_all(self) -> List[DeliveryStatus]:
        return self._session.query(DeliveryStatus).all()

    def find_by_id(self, status_id: int) -> Optional[DeliveryStatus]:
        return self._session.query(DeliveryStatus).filter(DeliveryStatus.id == status_id).first()
