#!/usr/bin/python3
def list_division(my_list_1=[], my_list_2=[], list_length=0):
    result = []

    for i in range(list_length):
        try:
            # Attempt division and append the result
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result.append("division by 0")
        except TypeError:
            # Handle non-numeric types
            print("wrong type")
            result.append("wrong type")
        except IndexError:
            # Handle out-of-range access
            print("out of range")
            result.append("out of range")

    return result
