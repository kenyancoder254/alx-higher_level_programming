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
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
