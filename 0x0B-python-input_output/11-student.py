#!/usr/bin/python3
"""module"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation"""
        student_dict = {}
        if attrs is None:
            for attr in self.__dict__:
                student_dict[attr] = self.__dict__[attr]
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    student_dict[attr] = self.__dict__[attr]

        return student_dict

    def reload_from_json(self, json):
        """Reloads from a dictionary.
        """
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
