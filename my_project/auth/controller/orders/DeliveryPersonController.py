from typing import List
from my_project.auth.dao.orders.DeliveryPersonDAO import DeliveryPersonDAO
from my_project.auth.domain.orders.DeliveryPerson import DeliveryPerson

class DeliveryPersonController:
    _dao = DeliveryPersonDAO()

    def find_all(self) -> List[DeliveryPerson]:
        return self._dao.find_all()

    def create(self, delivery_person: DeliveryPerson) -> None:
        self._dao.create(delivery_person)

    def find_by_id(self, delivery_person_id: int) -> DeliveryPerson:
        return self._dao.find_by_id(delivery_person_id)

    def update(self, delivery_person_id: int, delivery_person: DeliveryPerson) -> None:
        self._dao.update(delivery_person_id, delivery_person)

    def delete(self, delivery_person_id: int) -> None:
        self._dao.delete(delivery_person_id)
