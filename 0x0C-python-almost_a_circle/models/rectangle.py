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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter function"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter function"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter function"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Computes area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display a rectangle pattern based on widht and height"""
        for i in range(self.__height):
            print("#" * self.__width)
