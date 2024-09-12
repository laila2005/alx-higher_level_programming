#!/usr/bin/python3

import sys

num_args = len(sys.argv) -1

if num_args == 1:
    print("{} argument:".format(num_args))
elif num_args == 0:
    print("{} argument.".format(num_args))
else:
    print("{} arguments:".format(num_args))

for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
