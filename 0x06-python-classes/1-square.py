#!/usr/bin/python3
"""
This module defines a class Square.
It defines a square by a private instance attribute size.
"""


class Square:
    """
    A class that defines a square by a private instance attribute: size.
    The size attribute is initialized during instantiation.
    """


def __init__(self, size):
    """
        Initialize a new Square instance with a private attribute size.
        Args:
            size: The size of the square.
        """
    self.__size = size
