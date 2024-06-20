#!/usr/bin/python3
"""Creates Empty class"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self, width, height):
        """Issues a warning"""
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        """Validates input value"""
        self.name = name
        self.value = value
        if isinstance(self.value, int) is not True:
            raise TypeError(f"{self.name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """initializes the values of a rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Parent class square that inherit"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
