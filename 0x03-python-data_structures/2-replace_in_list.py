#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position (like in C).
    Args:
        my_list (list): List containing elements.
        idx (int): Index where the replacement should happen.
        element: New element to place at the given index.
    Returns:
        The modified list if index is valid,
        otherwise returns the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[idx]
    my_list[idx] = element
    return my_list
