#!/usr/bin/python3

def uppercase(s):
    """
    Prints a string in uppercase followed by a new line.

    Args:
    s (str): The string to convert to uppercase and print.
    """
    # Iterate through each character in the string
    for char in s:
        # Convert lowercase letters to uppercase by adjusting their Unicode code point
        if 'a' <= char <= 'z':
            # Convert lowercase character to uppercase
            char = chr(ord(char) - 32)
        print({}.format(char), end='')
    print()
