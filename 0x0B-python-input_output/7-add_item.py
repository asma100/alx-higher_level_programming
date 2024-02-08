#!/usr/bin/python3
"""
adding items
"""
import sys
"""module"""
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_file(items):
"""
    Adds items to a JSON file, creating the file if it doesn't exist.

    Args:
        items: A list of items to add to the file.

    Raises:
        ValueError: If the loaded JSON data is invalid.
    """
    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(items)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    items = sys.argv[1:]
    add_items_to_file(items)
