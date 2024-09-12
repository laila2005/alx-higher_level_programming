#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Check if there are any arguments to sum
    if len(sys.argv) > 1:
        # Convert all arguments to integers and sum them
        total_sum = sum(int(arg) for arg in sys.argv[1:])
    else:
        total_sum = 0

    # Print the result followed by a new line
    print(f"{total_sum}")
