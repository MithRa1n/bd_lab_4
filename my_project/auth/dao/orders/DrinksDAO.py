from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Drinks import Drink

class DrinksDAO(GeneralDAO):
    _domain_type = Drink

    def create(self, drink: Drink) -> None:
        self._session.add(drink)
        self._session.commit()

    def find_all(self) -> List[Drink]:
        return self._session.query(Drink).all()

    def find_by_id(self, drink_id: int) -> Optional[Drink]:
        return self._session.query(Drink).filter(Drink.id == drink_id).first()
