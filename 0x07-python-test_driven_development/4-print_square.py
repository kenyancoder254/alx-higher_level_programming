#!/usr/bin/python3
"""Prints a square using # character"""


def print_square(size):
    """
    Prints a square pattern using #

    Args:
        size(int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end='')
        print()
