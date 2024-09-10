#!/usr/bin/python3

def pow(a, b):
    """
    Computes a to the power of b and returns the result.

    Args:
        a (int or float): The base number.
        b (int): The exponent.

    Returns:
        float: The result of a raised to the power of b.
    """
 result = 1
    is_negative_exp = False

    if b < 0:
        is_negative_exp = True
        b = -b

    for _ in range(b):
        result *= a

    if is_negative_exp:
        result = 1 / result

    return result
