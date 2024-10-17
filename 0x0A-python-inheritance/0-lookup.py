#!/usr/bin/python3
"""
this module represents function that returns the
list of available attributes and methods of an object
"""


def lookup(obj):
    """returns a list of available attrbutes and methods"""
    return dir(obj)
