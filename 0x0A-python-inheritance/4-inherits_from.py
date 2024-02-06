#!/usr/bin/python3
"""module my list """


def inherits_from(obj, a_class):
    """
    obj :
    a_class :
    Returns : None
    """
    return isinstance(obj, a_class) and type(obj) != a_class
