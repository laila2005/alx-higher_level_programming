#!/usr/bin/python3

def pow(a, b):
    """
    Computes a to the power of b and returns the result.

    Args:
        a (int): The base number.
        b (int): The exponent.

    Returns:
        int: The result of a raised to the power of b.
    """
     if b < 0:
        a = 1 / a
        b = -b
    result = 1
    for _ in range(b):
        result *= a
    return result
