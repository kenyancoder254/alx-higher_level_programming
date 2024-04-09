#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    # Outer loop that decreases after iteration
    i = len(my_list) - 1
    while i > 1:
        j = 0
        while j < i:
            # check if element in prev index is greater
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i -= 1
    return my_list[-1]
