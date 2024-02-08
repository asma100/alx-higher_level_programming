#!/usr/bin/python3
""" My  module
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line

    Args:
        filename (str): file.
        search_string (str):  str search for
        new_string (str): strto insert after
    """

    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
