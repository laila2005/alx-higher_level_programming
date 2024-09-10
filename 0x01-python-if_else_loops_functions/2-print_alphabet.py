#!/usr/bin/python3

i = 'a'
while i <= 'z':
    print("{}".format(i), end="")
    i = chr(ord(i) + 1)
