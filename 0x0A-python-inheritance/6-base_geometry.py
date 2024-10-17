#!/usr/bin/python3
"""
this module includes a function that
its a Public instance method
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
