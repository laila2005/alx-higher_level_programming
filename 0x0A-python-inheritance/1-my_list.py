#!/usr/bin/python3
"""
this module represent
class MyList that inherits from list
"""


class MyList(list):
    """A subclass of list that provides a method to print the sorted list."""
    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
