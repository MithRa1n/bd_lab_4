from typing import List
from my_project.auth.dao.orders import DeliveryPersonDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import DeliveryPerson

class DeliveryPersonService(GeneralService):
    _dao = DeliveryPersonDAO

    def create(self, delivery_person: DeliveryPerson) -> None:
        self._dao.create(delivery_person)

    def get_all_delivery_persons(self) -> List[DeliveryPerson]:
        return self._dao.find_all()

    def get_delivery_person_by_id(self, delivery_person_id: int) -> DeliveryPerson:
        return self._dao.find_by_id(delivery_person_id)

    def update_delivery_person(self, delivery_person_id: int, delivery_person: DeliveryPerson) -> None:
        self._dao.update(delivery_person_id, delivery_person)

    def delete_delivery_person(self, delivery_person_id: int) -> None:
        self._dao.delete(delivery_person_id)
