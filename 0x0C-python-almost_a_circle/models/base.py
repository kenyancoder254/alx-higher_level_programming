#!/usr/bin/python3
"""
Creates first class Base to be used in the project
"""
import json


class Base:
    """First class Base to be used for the rest of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id with provided value and increments when none

        Args:
            id (int): Value of id
        """
        if id is not None:
            self.id = id
        else:
            Base.increment_nb_objects()
            self.id = Base.__nb_objects

    @classmethod
    def increment_nb_objects(cls, amount=1):
        """
        Increments private instance variable

        Args:
            amount (int): increment size
        """
        cls.__nb_objects += amount

    @classmethod
    def get_nb_objects(cls):
        """Returns incremented value of private instance variable"""
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return f"[]"
        else:
            json_string = json.dumps(list_dictionaries)
        return json_string
