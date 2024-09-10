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
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end='')  # Print without a newline after each character

    print()  # Print newline after the whole string
