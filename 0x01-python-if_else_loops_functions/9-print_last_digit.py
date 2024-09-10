def print_last_digit(number):
    """
    Prints the last digit of a number and returns it.

    Args:
        number (int): The number from which the last digit will be extracted.

    Returns:
        int: The last digit of the number.
    """
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
