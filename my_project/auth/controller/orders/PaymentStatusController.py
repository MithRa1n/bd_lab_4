from typing import List
from my_project.auth.dao.orders.PaymentStatusDAO import PaymentStatusDAO
from my_project.auth.domain.orders.PaymentStatus import PaymentStatus

class PaymentStatusController:
    _dao = PaymentStatusDAO()

    def find_all(self) -> List[PaymentStatus]:
        return self._dao.find_all()

    def create(self, status: PaymentStatus) -> None:
        self._dao.create(status)

    def find_by_id(self, status_id: int) -> PaymentStatus:
        return self._dao.find_by_id(status_id)

    def update(self, status_id: int, status: PaymentStatus) -> None:
        self._dao.update(status_id, status)

    def delete(self, status_id: int) -> None:
        self._dao.delete(status_id)
