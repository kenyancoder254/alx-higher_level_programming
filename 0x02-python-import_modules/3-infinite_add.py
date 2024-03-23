#!/usr/bin/python3
# print the result of addition of all arguments
from sys import argv
if __name__ == "__main__":
    if len(argv) < 2:
        print('0')
    else:
        i = 1
        result = 0
        while i < len(argv):
            num = int(argv[i])
            result += num
            i += 1
        print(result)
