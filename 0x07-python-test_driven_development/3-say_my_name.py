#!/usr/bin/python3
"""Prints the first and last name of user"""


def say_my_name(first_name, last_name=""):
    """
    Prints last and first name of the user

    Args:
        first_name(str): user's first name
        last_name(str): user's last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
