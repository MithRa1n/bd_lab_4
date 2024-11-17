from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.DeliveryPerson import DeliveryPerson

class DeliveryPersonDAO(GeneralDAO):
    _domain_type = DeliveryPerson

    def create(self, person: DeliveryPerson) -> None:
        self._session.add(person)
        self._session.commit()

    def find_all(self) -> List[DeliveryPerson]:
        return self._session.query(DeliveryPerson).all()

    def find_by_id(self, person_id: int) -> Optional[DeliveryPerson]:
        return self._session.query(DeliveryPerson).filter(DeliveryPerson.id == person_id).first()
