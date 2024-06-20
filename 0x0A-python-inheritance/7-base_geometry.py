#!/usr/bin/python3
"""Creates Empty class"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Issues a warning to the user"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input value"""
        self.name = name
        self.value = value
        if isinstance(self.value, int) is not True:
            raise TypeError(f"{self.name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
