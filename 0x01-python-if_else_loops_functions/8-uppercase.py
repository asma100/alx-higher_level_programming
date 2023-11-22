#!/usr/bin/python3

def uppercase(input_str):
    """Prints a string in uppercase followed by a new line.

    Args:
        input_str (str): The string to print in uppercase.
    """
    for char in input_str:
        print("{}".format(chr(ord(char) - 32)) if 97 <= ord(char) <= 122 else "{}".format(char), end="")
    print()
