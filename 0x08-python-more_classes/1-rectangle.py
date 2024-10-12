#!/usr/bin/python3
"""
this module  defines a rectangle class.
"""


class Rectangle:
    """
    class that defines a rectangle by its width
    and hight
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
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
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
