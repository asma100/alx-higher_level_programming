#!/usr/bin/python3
"""read file """
import json
"""json module """


def load_from_json_file(filename):
    """ from file  JSON
    """
    with open(filename, "r") as f:
        return json.load(f)
