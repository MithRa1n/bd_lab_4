from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Salad import Salad

class SaladDAO(GeneralDAO):
    _domain_type = Salad

    def create(self, salad: Salad) -> None:
        self._session.add(salad)
        self._session.commit()

    def find_all(self) -> List[Salad]:
        return self._session.query(Salad).all()

    def find_by_id(self, salad_id: int) -> Optional[Salad]:
        return self._session.query(Salad).filter(Salad.id == salad_id).first()
