#!/usr/bin/python3
"""
Implements function that creates an object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from JSON file

    Args:
        filename(str): name of json file
    """
    with open(filename, 'r') as file:
        return json.load(file)
