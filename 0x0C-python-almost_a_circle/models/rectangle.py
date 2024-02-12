#!/usr/bin/python3
"""module Rectangle"""
from models.base import Base
"""import Base"""


class Rectangle (Base):
    """Rectangle class that inherits  from Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__set_width(width)
        self.__set_height(height)
        self.__set_x(x)
        self.__set_y(y)

    def __set_width(self, value):
        """set w"""
        if isinstance(value, int) and value > 0:
            self.__width = value
        else:
            raise ValueError("Width must be a positive integer.")

    def __get_width(self):
        """get w"""
        return self.__width

    def __set_height(self, value):
        """set h"""
        if isinstance(value, int) and value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be a positive integer.")

    def __get_height(self):
        """get h"""
        return self.__height

    def __set_x(self, value):
        """set x"""
        if isinstance(value, int):
            self.__x = value
        else:
            raise ValueError("x must be an integer.")

    def __get_x(self):
        """get x"""
        return self.__x

    def __set_y(self, value):
        """set y"""
        if isinstance(value, int):
            self.__y = value
        else:
            raise ValueError("y must be an integer.")

    def __get_y(self):
        """get y"""
        return self.__y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__get_width()

    @width.setter
    def width(self, value):
        """Setter for the width """
        self.__set_width(value)

    @property
    def height(self):
        """Getter for the height """
        return self.__get_height()

    @height.setter
    def height(self, value):
        """Setter for the height """
        self.__set_height(value)

    @property
    def x(self):
        """Getter for the x """
        return self.__get_x()

    @x.setter
    def x(self, value):
        """Setter for the x"""
        self.__set_x(value)

    @property
    def y(self):
        """Getter for the y"""
        return self.__get_y()

    @y.setter
    def y(self, value):
        """Setter for the y"""
        self.__set_y(value)
