#!/usr/bin/python3
def safe_print_integer(value):
    int(value)
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
