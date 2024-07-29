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
