#!/usr/bin/python3
"""
this module represents a
class Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class with an area method and integer validator."""

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that defines a rectangle based on BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a new Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

print(issubclass(Rectangle, BaseGeometry))        
