#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_digit = abs(number) % 10 * -1
else:
    l_digit = number % 10
if l_digit > 5:
    print(f"Last digit of {number:d} is\
 {l_digit:d} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number:d} is {l_digit:d} and is 0")
elif l_digit < 0 and l_digit != 0:
    print(f'Last digit of {number:d} is\
 {l_digit:d} and is less than 6 and not 0')
