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

    def set_size(self, value):
        """Sets the value for size

        Args:
            param1 (int): self reference for class
            param2(int): size

        Returns:
            novalue: it will set the value of size
        """
        if type(value) is not int:
            raise TypeError(f"size must be an integer")
        if value < 0:
            raise ValueError(f"size must be >= 0")
        self._size = value
