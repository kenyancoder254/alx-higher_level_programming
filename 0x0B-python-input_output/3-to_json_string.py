#!/usr/bin/python3
import json
"""
Implements function to return JSON rep of an object
"""


def to_json_string(my_obj):
    """
    Serializes a python object

    Args:
        my_obj(str): python object
    """
    json_string = json.dumps(my_obj)
    return json_string
