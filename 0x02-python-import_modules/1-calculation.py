#!/usr/bin/python3
from calculator_1 import add , sub , mul, div

if __name__ == '__main__':
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    
    result = div(a, b)
    if result.is_integer():  # Check if the division result is a whole number
        result = int(result)
    print("{} / {} = {}".format(a, b, result))
