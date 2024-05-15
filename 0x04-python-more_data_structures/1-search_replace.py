#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # use enumerate function to get index and values of the list
    modified = []
    modified = my_list.copy()
    for index, value in enumerate(modified):
        if value == search:
            position = modified.index(value)
            modified[position] = replace
    return modified
