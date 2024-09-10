#!/usr/bin/python3


def islower(c):
    """
    Returns True if c is a lowercase character, False otherwise.
    """
    # Use the ord() function to get the ASCII value of the character
    ascii_val = ord(c)
    
    # Check if the ASCII value falls within the range of lowercase letters
    if 97 <= ascii_val <= 122:
        return True
    else:
        return False
