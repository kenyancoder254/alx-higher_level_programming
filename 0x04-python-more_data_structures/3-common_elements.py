#!/usr/bin/python3
def common_elements(set_1, set_2):
    list(set_1)
    list(set_2)
    multiple_element = []
    combined_list = [*set_1, *set_2]
    for values in combined_list:
        counter = combined_list.count(values)
        if counter > 1:
            multiple_element.append(values)
    return set(multiple_element)
