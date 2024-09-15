#!/usr/bin/env python3
def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C'
    from the input string and returns the result.
    Parameters:
    my_string (str): The string from which
    characters 'c' and 'C' will be removed.
    Returns:
    str: The modified string with 'c' and 'C' removed.
    """
    result = []
    for char in my_string:
        if char != 'c' and char != 'C':
            result.append(char)
    return ''.join(result)
