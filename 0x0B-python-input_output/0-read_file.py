#!/usr/bin/python3
"""
Implements a function to read a text file
"""


def read_file(filename=""):
    """
    Reads a text file in UTF8 format & prints to stdout

    Args:
        filename(str): file to be read
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        content = file.read()
    print(content, end="")
