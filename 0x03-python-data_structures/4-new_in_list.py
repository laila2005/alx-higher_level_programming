#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Returns a new list with the element at `idx` replaced by `element`.
    If `idx` is out of range, returns a copy of the original list.
    Parameters:
    my_list (list): The original list.
    idx (int): The index to replace.
    element: The new element to insert.
    """
    copied_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copied_list
    copied_list[idx] = element
    return copied_list
