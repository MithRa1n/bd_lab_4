from typing import List
from my_project.auth.dao.orders import DeliveryStatusDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import DeliveryStatus

class DeliveryStatusService(GeneralService):
    _dao = DeliveryStatusDAO

    def create(self, delivery_status: DeliveryStatus) -> None:
        self._dao.create(delivery_status)

    def get_all_delivery_statuses(self) -> List[DeliveryStatus]:
        return self._dao.find_all()

    def get_delivery_status_by_id(self, delivery_status_id: int) -> DeliveryStatus:
        return self._dao.find_by_id(delivery_status_id)

    def update_delivery_status(self, delivery_status_id: int, delivery_status: DeliveryStatus) -> None:
        self._dao.update(delivery_status_id, delivery_status)

    def delete_delivery_status(self, delivery_status_id: int) -> None:
        self._dao.delete(delivery_status_id)
