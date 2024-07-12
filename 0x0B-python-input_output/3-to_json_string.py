#!/usr/bin/python3
"""
Serializes a python obj to json string
"""
import json


def to_json_string(my_obj):
    """
    Serializes a python object

    Args:
        my_obj(str): python object
    """
    json_string = json.dumps(my_obj)
    return json_string
