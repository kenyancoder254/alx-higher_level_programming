#!/usr/bin/python3
"""Creates a class square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of square

        Args:
            size (int): size of the square
            x (int): vertical
            y (int): horizontal
            id (int): identification of the instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints string rep of the class to stdout"""
        return (
                f"[Square] ({self.id})"
                f" {self.x}/{self.y} - {self.width}"
                )

    @property
    def size(self):
        """size getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary rep of square"""
        dict_rep = {"id": self.id, "size": self.width,
                    "x": self.x, "y": self.y}
        return dict_rep
