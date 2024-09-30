#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []  # This will hold the result of divisions

    for i in range(list_length):
        try:
            # Try to perform the division
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            # Handle wrong type (non-integer/float)
            print("wrong type")
            result = 0
        except IndexError:
            # Handle out-of-range for either list
            print("out of range")
            result = 0
        finally:
            # Append the result (either valid or 0) to the result list
            result_list.append(result)

    return result_list
