#!/usr/bin/python3
"""read file """
import json
"""json module """


def save_to_json_file(my_obj, filename):
    """object to a text file as JSON
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
