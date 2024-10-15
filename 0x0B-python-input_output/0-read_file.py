#!/usr/bin/python
"""
this module reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
