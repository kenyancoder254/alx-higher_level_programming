#!/usr/bin/python3
""" MyList class will inherit from parent list"""


class MyList(list):
    """ Inherits a list"""
    def print_sorted(self):
        """Prints a sorted list of numbers"""
        sorted_list = sorted(self)
        print(sorted_list)
