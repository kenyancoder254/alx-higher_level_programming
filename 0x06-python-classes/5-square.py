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
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square based on size"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError(f"size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
