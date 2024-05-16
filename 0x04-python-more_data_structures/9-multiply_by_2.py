#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    keys = list(new_dictionary)
    for n in keys:
        new_dictionary[n] = new_dictionary[n] * 2
    return new_dictionary
