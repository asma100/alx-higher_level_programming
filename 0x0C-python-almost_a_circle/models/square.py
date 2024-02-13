#!/usr/bin/python3
"""module Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    @property
    def size(self):
        """
        Gets the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        """
        self.int_validate("size", value)
        self.width = self.height = value
