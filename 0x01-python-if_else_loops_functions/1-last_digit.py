#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = abs(number) % 10 * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print("Last digit of {number:d} is {last_digit:d} and is greater than 5".format(number=number,last_digit=last_digit))
elif last_digit == 0:
    print("Last digit of {number:d} is {last_digit:d} and is 0".format(number=number, last_digit=last_digit))
elif last_digit < 0 and last_digit != 0:
    print('Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0'.format(number=number, last_digit=last_digit))