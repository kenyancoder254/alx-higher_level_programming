#!/usr/bin/python3
"""
Implements function that writes an object to text file in JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to text file using JSON
    Args:
        my_obj(object): python object
        file_name(str): text file
    """
    json_string = json.dumps(my_obj)
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(json_string)
