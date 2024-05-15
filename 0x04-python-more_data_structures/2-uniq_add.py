#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set(my_list)
    list(unique_values)
    for value in unique_values:
        unique_values.add(value)
    return sum(unique_values)
