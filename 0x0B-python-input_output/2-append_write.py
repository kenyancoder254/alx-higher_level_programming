#!/usr/bin/python3
"""
Appends string to end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends string to end of text file

    Args:
        filename(str): name of file
        text(str): data to input

    Returns:
        int: no. of characters appended
    """
    with open(filename, 'a', encoding="UTF8") as file:
        content = file.write(text)
    return content
