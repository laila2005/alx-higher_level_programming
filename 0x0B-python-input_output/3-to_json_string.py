#!/usr/bin/python3
import json
"""
This module provides a function
that returns the JSON representation of an object.
"""

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to convert to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
