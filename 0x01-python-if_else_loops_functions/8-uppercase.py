#!/usr/bin/python3

def uppercase(s):
    """
    Prints a string in uppercase
    followed by a new line.

    Args:
        s (str): The string to convert to
        uppercase and print.
    """
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        result += char
    print("{}\n".format(result))
         
