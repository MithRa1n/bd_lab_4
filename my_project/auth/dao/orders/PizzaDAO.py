from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Pizza import Pizza

class PizzaDAO(GeneralDAO):
    _domain_type = Pizza

    def create(self, pizza: Pizza) -> None:
        self._session.add(pizza)
        self._session.commit()

    def find_all(self) -> List[Pizza]:
        return self._session.query(Pizza).all()

    def find_by_id(self, pizza_id: int) -> Optional[Pizza]:
        return self._session.query(Pizza).filter(Pizza.id == pizza_id).first()