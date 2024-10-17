#!/usr/bin/python3
"""
this module represent a class
"""


class BaseGeometry:
    """
    A class that serves as a base for geometrical shapes.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        Raises an Exception if the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""
        if value is None:
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
