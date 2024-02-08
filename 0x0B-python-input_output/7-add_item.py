#!/usr/bin/python3


import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a text file as JSON.

    Args:
        my_obj: The object to serialize and save.
        filename: The name of the file to save to.
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Loads a JSON object from a file.

    Args:
        filename: The name of the file to load from.

    Returns:
        The loaded JSON object.
    """

    with open(filename, "r") as f:
        return json.load(f)


def add_items_to_file(items: list[str]) -> None:
    """
    Adds items to a JSON file, creating the file if it doesn't exist.

    Args:
        items: A list of items to add to the file.
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
