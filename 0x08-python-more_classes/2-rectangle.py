#!/usr/bin/python3
"""
this module defines a rectangle class.
"""


class Rectangle:
    """
    class that defines a rectangle h and w.
    """
    def __init__(self, width=0, height=0):
        """
        initializes a rectangle with h and w
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter method for the w arttibutes
        """
        return self.width

    @width.setter
    def width(self, value):
        """
        setter method for the width attribute.
        Ensures the width is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Ensures the height is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If either width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
