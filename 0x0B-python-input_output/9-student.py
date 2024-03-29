#!/usr/bin/python3
""" My  module
"""


class Student:
    """student : first name, last name, age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
