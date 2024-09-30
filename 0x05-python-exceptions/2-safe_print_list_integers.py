#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    for i in range(x):
        try:
            # Attempt to print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Increment count if successfully printed
        except (ValueError, TypeError):
            # If the element is not an integer, silently skip it
            continue
        except IndexError:
            # If x is larger than the list, break when out of range
            raise
    print()  # Print a newline at the end
    return count  # Return the number of integers successfully printed
