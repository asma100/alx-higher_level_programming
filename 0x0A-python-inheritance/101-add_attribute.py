#!/usr/bin/python3
""" My  module
"""


def add_attribute(object, key, value):
    """ADD attribute"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, key, value)
