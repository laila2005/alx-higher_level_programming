#!/usr/bin/python3
"""
this module represent a class
that inherits from BaseGeometry
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
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Returns a detailed string representation of the rectangle."""
        return f"Rectangle(width={self.__width}, height={self.__height})"
