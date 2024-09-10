#!/usr/bin/python3


def islower(c):
    """
    Checks if the character is a lowercase letter.

    Args:
    c (str): The character to check.

    Returns:
    bool: True if c is a lowercase letter, False otherwise.
    """
     if len(c) != 1:
        raise ValueError("Input must be a single character string.")
    return 'a' <= c <= 'z'
