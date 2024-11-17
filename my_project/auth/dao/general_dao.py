"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

from my_project import db


class GeneralDAO(ABC):
    """
    The common realization of Data Access class.
    """
    _domain_type = None
    _session = db.session

    def find_all(self) -> List[object]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._session.query(self._domain_type).all()

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key.
        :param key: integer key (surrogate primary key)
        :return: search object
        """
        return self._session.query(self._domain_type).get(key)

    def create(self, obj: object) -> object:
        """
        Creates object in database table.
        :param obj: object to create in Database
        :return: created object
        """
        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, obj_list: List[object]) -> List[object]:
        """
        Creates objects from object list.
        :param obj_list: object list to create in Database
        :return: list of created object
        """
        self._session.add_all(obj_list)
        self._session.commit()
        return obj_list

    def update(self, key: int, in_obj: object) -> None:
        """
        Updates object in database table
        :param key: integer key (surrogate primary key)
        :param in_obj: object to update in Database
        """
        domain_obj = self._session.query(self._domain_type).get(key)
        mapper: Mapper = inspect(type(in_obj))  # Metadata
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()

    def patch(self, key: int, field_name: str, value: object) -> None:
        """
        Modifies defined field of object in database table.
        :param key: integer key (surrogate primary key)
        :param field_name: field name of object
        :param value: field value of object
        """
        domain_obj = self._session.query(self._domain_type).get(key)
        setattr(domain_obj, field_name, value)
        self._session.commit()

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key.
        :param key: integer key (surrogate primary key)
        """
        domain_obj = self._session.query(self._domain_type).get(key)
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise 

    def delete_all(self) -> None:
        """
        Deletes all objects from database table.
        """
        self._session.query(self._domain_type).delete()
        self._session.commit()
