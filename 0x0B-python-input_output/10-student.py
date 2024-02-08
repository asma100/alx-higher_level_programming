#!/usr/bin/python3
""" My  module
"""


class Student:
    """Represents a student with their first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary Student
        """
        student_dict = {}
        if attrs is None:
            for attr in self.__dict__:
                student_dict[attr] = self.__dict__[attr]
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    student_dict[attr] = self.__dict__[attr]

        return student_dict
