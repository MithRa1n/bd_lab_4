

from abc import ABC
from typing import List, Dict

from http import HTTPStatus
from flask import abort


class GeneralController(ABC):
    """
    The common realization of controller.
    """
    _service = None

    def find_all(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        # return list(map(lambda x: x.put_into_dto(), self._service.find_all()))
        return [x.put_into_dto() for x in self._service.find_all()]

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto()

    def create(self, obj: object) -> object:
        """
        Creates object in database table using Service layer.
        :param obj: object to create in Database
        :return: DTO for created object
        """
        return self._service.create(obj).put_into_dto()

    def create_all(self, obj_list: List[object]) -> List[object]:
        """
        Creates objects from object list using Service layer.
        :param obj_list: object list to create in Database
        :return: list of created objects as DTOs
        """
        return list(map(lambda x: x.put_into_dto(), self._service.create(obj_list)))

    def update(self, key: int, new_obj: object) -> None:
        """
        Updates object in database table using Service layer.
        :param key: integer key (surrogate primary key)
        :param new_obj: object to create in Database
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(key, new_obj)

    def patch(self, key: int, value_dict: Dict[str, object]) -> None:
        """
        Modifies defined field of object in database table using Service layer.
        :param key: integer key (surrogate primary key)
        :param value_dict: key-values
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        for field_name, value in value_dict.items():
            self._service.patch(key, field_name, value)

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key from Service layer.
        :param key: integer key (surrogate primary key)
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(key)

    def delete_all(self) -> None:
        """
        Deletes all objects from database table using Service layer.
        """
        self._service.delete_all()
