#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    combined_set = set_1.union(set_2)
    return sorted(combined_set)
