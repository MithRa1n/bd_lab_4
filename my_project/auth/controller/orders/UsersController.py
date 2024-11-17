from typing import List
from my_project.auth.dao.orders.UsersDAO import UsersDAO
from my_project.auth.domain.orders.Users import Users

class UsersController:
    _dao = UsersDAO()

    def find_all(self) -> List[Users]:
        return self._dao.find_all()

    def create(self, user: Users) -> None:
        self._dao.create(user)

    def find_by_id(self, user_id: int) -> Users:
        return self._dao.find_by_id(user_id)

    def update(self, user_id: int, user: Users) -> None:
        self._dao.update(user_id, user)

    def delete(self, user_id: int) -> None:
        self._dao.delete(user_id)
