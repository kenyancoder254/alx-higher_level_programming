#!/usr/bin/python3
"""
Writes string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes text to a file

    Args:
        filename(str): name of file
        text(str): line to be writen

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding="UTF8") as file:
        content = file.write(text)
    return content
