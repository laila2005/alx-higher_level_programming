#!/usr/bin/python3


def islower(c):
    """
    Checks if the character is a lowercase letter.

    Args:
    c (str): The character to check.

    Returns:
    bool: True if c is a lowercase letter, False otherwise.
    """
     if not isinstance(c, str):
        raise TypeError("Input must be a string.")
    if len(c) != 1:
        raise ValueError("Input must be a single character string.")
    return 'a' <= c <= 'z'
