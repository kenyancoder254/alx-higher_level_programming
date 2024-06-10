#!/usr/bin/python3


""" Defines class square based on 1-square.py"""


class Square:
    """Stores the value for square"""
    def __init__(self, size=0):
        """Initializes square and raises TypeError and ValueError respectively

        Args:
            param1 (int): Size of the square


        """
        if not isinstance(size, int):
            raise TypeError(f"size must be an integer")
        elif size < 0:
            raise ValueError(f"Size must be >= 0")
        self.__size = size
