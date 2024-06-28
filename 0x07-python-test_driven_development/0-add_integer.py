#!/usr/bin/python3
"""
Finds the sum of 2 integers
a will be initialized
b will have a default value of 98 if not initialized
"""


def add_integer(a, b=98):
    """
    Adds 2 integers or floats after casting them
    """
    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
