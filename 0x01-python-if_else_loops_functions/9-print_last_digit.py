#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit

    Args:
        number (int): The number

    Returns:
        int:  last digit.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
