#!/usr/bin/env python3
def no_c(my_string):
    char_removed = ['c', 'C']
    filtered = (char for char in my_string if char not in char_removed)
    modified_string = ''.join(filtered)
    return modified_string
