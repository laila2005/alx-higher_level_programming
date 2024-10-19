#!/usr/bin/python3
"""
Module models.base
This module contains a class Base
"""

class Base:
    """
    Base class for future classes.
    It manages the 'id' attribute and avoids code duplication.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor to initialize the 'id' attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
