#!/usr/bin/python3
"""module my list """
def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return   type(obj) == a_class

