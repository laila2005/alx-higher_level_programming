#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    # Add elements that are in set_1 but not in set_2
    for x in set_1:
        if x not in set_2:
            new_list.append(x)
    # Add elements that are in set_2 but not in set_1
    for x in set_2:
        if x not in set_1:
            new_list.append(x)
    return new_list
