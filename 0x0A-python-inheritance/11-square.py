#!/usr/bin/python3
"""Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A sub subclass  """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area """
        return self.__size ** 2

    def __str__(self):
        """Returns"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
