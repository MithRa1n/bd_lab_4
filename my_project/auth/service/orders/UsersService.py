from typing import List
from my_project.auth.dao.orders import UsersDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Users

class UserService(GeneralService):
    _dao = UsersDAO

    def create(self, user: Users) -> None:
        self._dao.create(user)

    def get_all_users(self) -> List[Users]:
        return self._dao.find_all()

    def get_user_by_id(self, user_id: int) -> Users:
        return self._dao.find_by_id(user_id)

    def update_user(self, user_id: int, user: Users) -> None:
        self._dao.update(user_id, user)

    def delete_user(self, user_id: int) -> None:
        self._dao.delete(user_id)
