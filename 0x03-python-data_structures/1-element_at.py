#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specific index like in C.
    Args:
        my_list (list): List containing elements.
        idx (int): Index of the element to retrieve.
    Returns:
        Element at the specified index,
        or None if the index is out of range or negative.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
