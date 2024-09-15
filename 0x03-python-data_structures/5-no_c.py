#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for o in my_string:
        if o != 'c' and o != 'C':
            new_string.append(o)
    return ''.join(new_string)
