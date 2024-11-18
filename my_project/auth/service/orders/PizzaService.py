from typing import List
from my_project.auth.dao.orders import PizzaDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Pizza

class PizzaService(GeneralService):
    _dao = PizzaDAO

    def create(self, pizza: Pizza) -> None:
        self._dao.create(pizza)

    def get_all_pizzas(self) -> List[Pizza]:
        return self._dao.find_all()

    def get_pizza_by_id(self, pizza_id: int) -> Pizza:
        return self._dao.find_by_id(pizza_id)

    def update_pizza(self, pizza_id: int, pizza: Pizza) -> None:
        self._dao.update(pizza_id, pizza)

    def delete_pizza(self, pizza_id: int) -> None:
        self._dao.delete(pizza_id)