#!/usr/bin/python3


"""Defines rectangle based on 0-rectangle.py"""


class Rectangle:
    """Describes properties of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes Rectangle with private attribute width

        Args:
            param(1) (int): Width of the rectangle
            param(2) (int): height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
