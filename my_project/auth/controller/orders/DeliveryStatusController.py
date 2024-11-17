from typing import List
from my_project.auth.dao.orders.DeliveryStatusDAO import DeliveryStatusDAO
from my_project.auth.domain.orders.DeliveryStatus import DeliveryStatus

class DeliveryStatusController:
    _dao = DeliveryStatusDAO()

    def find_all(self) -> List[DeliveryStatus]:
        return self._dao.find_all()

    def create(self, status: DeliveryStatus) -> None:
        self._dao.create(status)

    def find_by_id(self, status_id: int) -> DeliveryStatus:
        return self._dao.find_by_id(status_id)

    def update(self, status_id: int, status: DeliveryStatus) -> None:
        self._dao.update(status_id, status)

    def delete(self, status_id: int) -> None:
        self._dao.delete(status_id)
