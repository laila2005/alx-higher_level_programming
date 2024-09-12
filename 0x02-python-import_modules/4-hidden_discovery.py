#!/usr/bin/python3

import hidden_4
import sys

if __name__ == "__main__":
    # Get all the names defined in the module
    names = dir(hidden_4)
    # Filter out names that start with __
    filtered_names = [name for name in names if not name.startswith("__")]
    # Sort names alphabetically
    filtered_names.sort()
    # Print each name on a new line
    for name in filtered_names:
        print(name)
