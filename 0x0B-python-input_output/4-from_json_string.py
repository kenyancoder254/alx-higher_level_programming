#!/usr/bin/python3
"""
Deserializes a json string to python object
"""
import json


def from_json_string(my_str):
    """
    Decodes json string

    Args:
        my_str(str): json string
    """
    python_object = json.loads(my_str)
    return python_object
