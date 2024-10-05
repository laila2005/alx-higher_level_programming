#!/usr/bin/python3
import unittest

def add_integer(a, b=98):
    """ adding two integrs a , b.

    Args:
        a:the 1st number should be int
        b:the 2nd number by defult = 98, should be int
    returns:
        the sum of two numbers
    raises:
        TypeError: If a or b is not an integer or a float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2.5, 3)
        5
        >>> add_integer(10)
        108
        >>> add_integer("a", 2)
        Traceback (most recent call last):
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
