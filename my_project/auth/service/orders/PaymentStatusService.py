from typing import List
from my_project.auth.dao.orders import PaymentStatusDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import PaymentStatus

class PaymentStatusService(GeneralService):
    _dao = PaymentStatusDAO

    def create(self, payment_status: PaymentStatus) -> None:
        self._dao.create(payment_status)

    def get_all_payment_statuses(self) -> List[PaymentStatus]:
        return self._dao.find_all()

    def get_payment_status_by_id(self, payment_status_id: int) -> PaymentStatus:
        return self._dao.find_by_id(payment_status_id)

    def update_payment_status(self, payment_status_id: int, payment_status: PaymentStatus) -> None:
        self._dao.update(payment_status_id, payment_status)

    def delete_payment_status(self, payment_status_id: int) -> None:
        self._dao.delete(payment_status_id)
