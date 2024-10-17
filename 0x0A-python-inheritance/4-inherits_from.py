#!/usr/bin/python3
"""
this module Checks if an object is an
instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
