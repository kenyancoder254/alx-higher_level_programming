#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary))
    for n in keys:
        print("{}: {}".format(n, a_dictionary[n]))
