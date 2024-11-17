from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PaymentStatus import PaymentStatus

class PaymentStatusDAO(GeneralDAO):
    _domain_type = PaymentStatus

    def create(self, status: PaymentStatus) -> None:
        self._session.add(status)
        self._session.commit()

    def find_all(self) -> List[PaymentStatus]:
        return self._session.query(PaymentStatus).all()

    def find_by_id(self, status_id: int) -> Optional[PaymentStatus]:
        return self._session.query(PaymentStatus).filter(PaymentStatus.id == status_id).first()
