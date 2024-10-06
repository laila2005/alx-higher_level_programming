#!/usr/bin/python3
"""
this module prints a square with the character #
"""


def print_square(size):
    """
     prints a square with the character #

     Args: size

     raises:
        if size < 0:
        raise ValueError

        if size not an integer
        raise TypeError size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int)):
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
