#!/usr/bin/python3
"""Formats text input"""


def text_indentation(text):
    """
    Prints a text with 2 lines after '.' '?' and ':' characters

    Args:
        text(str): input string to be formated
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    search_chars = {'.', '?', ':'}
    result = ""
    i = 0
    while i < len(text):
        if text[i] in search_chars:
            result += text[i] + "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            result += text[i]
            i += 1
    print(result, end="")
