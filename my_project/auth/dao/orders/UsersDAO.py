from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Users import Users

class UsersDAO(GeneralDAO):
    _domain_type = Users

    def create(self, user: Users) -> None:
        self._session.add(user)
        self._session.commit()

    def find_all(self) -> List[Users]:
        return self._session.query(Users).all()

    def find_by_id(self, user_id: int) -> Optional[Users]:
        return self._session.query(Users).filter(Users.id == user_id).first()
