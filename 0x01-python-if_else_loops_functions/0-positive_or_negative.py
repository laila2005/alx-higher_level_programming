#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{number:d} is positive".format(number=number))
elif number < 0:
    print("{number:d} is negative".format(number=number))
else:
    print("{number:d} is zero".format(number=number))
