def safe_print_division(a, b):
    result = None
    try:
        # Attempt the division
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero
        result = None
    finally:
        # This block always runs, print the result
        print("Inside result: {}".format(result))
    return result  # Return the result or None
