#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print("{:02d}".format(number), end=", ")
    else:
        print("{}".format(number), end=", ")
