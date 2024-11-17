from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Toppings import Topping

class ToppingsDAO(GeneralDAO):
    _domain_type = Topping

    def create(self, topping: Topping) -> None:
        self._session.add(topping)
        self._session.commit()

    def find_all(self) -> List[Topping]:
        return self._session.query(Topping).all()

    def find_by_id(self, topping_id: int) -> Optional[Topping]:
        return self._session.query(Topping).filter(Topping.topping_id == topping_id).first()
