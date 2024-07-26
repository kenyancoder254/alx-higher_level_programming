#!/usr/bin/python3
"""Creates derived class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Creates derived class rectangle and initializes it"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes class with values

        Args:
            width (int): width of rectangle
            height (int): height of rect...
            x (int): x axis
            y (int): y axis
            id (int): identification
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter function"""
        self.__width = value

    @property
    def height(self):
        """Height getter function"""
        return sef.__height

    @height.setter
    def height(self, value):
        """height setter function"""
        self.__height = value

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter function"""
        self.__x = value

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter function"""
        self.__y = y
