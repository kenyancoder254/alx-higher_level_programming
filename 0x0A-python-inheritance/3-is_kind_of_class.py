#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if an object is an instance ofa class"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
