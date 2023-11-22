#!/usr/bin/python3

def uppercase(input_str):
    """Prints a string in uppercase followed by a new line.

    Args:
        input_str (str): The string to print in uppercase.
    """
    for char in input_str:
        if ord(char) >= 97 and ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
