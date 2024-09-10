#!/usr/bin/python3

# Print all possible different combinations of two digits
for i in range(10):
    for j in range(i + 1, 10):
        # Print combination with formatting
        print(f"{}{}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
