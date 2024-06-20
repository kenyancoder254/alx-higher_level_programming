#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """Checks for inheritance either directly or indirectly"""
    obj_class = obj.__class__
    if issubclass(obj_class, a_class) is True:
        return True
    else:
        return False
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
