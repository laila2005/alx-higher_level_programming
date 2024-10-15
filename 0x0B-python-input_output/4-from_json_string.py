#!/usr/bin/python3
import json
"""
This module provides a function
that returns a Python object
from a JSON string representation.
"""

def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
