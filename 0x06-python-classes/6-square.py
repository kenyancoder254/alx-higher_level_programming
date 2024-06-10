#!/usr/bin/python3


""" Defines class square based on 1-square.py"""


class Square:
    """Stores the value for square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square and raises TypeError and ValueError respectively

        Args:
            param1 (int): Size of the square


        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) and len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) == 2 and \
        all(isinstance(num, int) for num in value) and all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of positive integers")
        self.__position = value

    def area(self):
        return self.__position * self.__position

    def my_print(self):
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
