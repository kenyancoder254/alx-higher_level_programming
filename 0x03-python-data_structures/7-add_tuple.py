#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) and len(tuple_b) == 2:
        new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
        return new_tuple
    elif len(tuple_a) < 2:
        new_tuple = ((tuple_a[0] + tuple_b[0]), (0 + tuple_b[1]))
        return new_tuple
    elif len(tuple_b) < 2:
        new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0))
        return new_tuple
