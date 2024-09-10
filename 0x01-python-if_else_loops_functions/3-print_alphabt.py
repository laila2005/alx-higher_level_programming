#!/usr/bin/python3

i = 'a'
while i <= 'z':
    if i != 'q' and i != 'e':
        print("{}".format(i), end="")
    i = chr(ord(i) + 1)
