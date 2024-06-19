#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
