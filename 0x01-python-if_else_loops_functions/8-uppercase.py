#!/usr/bin/python3


def uppercase(str):
    """Prints a string in uppercase followed by a new line.

    Args:
        str (str): The string to print in uppercase.
    """
    for i in str:
       
        if ord(i) >= 97 and ord(i) <= 122:
           
           
            print(chr(ord(i) - 32), end="")
        else:
           
            print(i, end="")
    print()
