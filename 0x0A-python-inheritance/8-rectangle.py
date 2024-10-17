from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle based on BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a new Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute
