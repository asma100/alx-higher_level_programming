#!/usr/bin/python3
"""module Rectangle"""
from models.base import Base
"""import Base"""


class Rectangle(Base):
    """A rectangle with a width, height, x-coordinate, and y-coordinate."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object.

        """

        self.int_validate("width", width, False)
        self.int_validate("height", height, False)
        self.int_validate("x", x, True)
        self.int_validate("y", y, True)

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def int_validate(self, name, value, non_negative):
        """
        Validates that the given value is a positive integer.

        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if non_negative and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.int_validate("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.int_validate("height", value, True)
        self.__width = value

    @property
    def x(self):
        """Getter for the x-coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x-coordinate attribute."""
        self.int_validate("x", value, True)
        self.__x = value

    @property
    def y(self):
        """Getter for the y-coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y-coordinate attribute."""
        self.int_validate("y", value, True)
        self.__y = value

    def area(self):
        """area of rectangle."""
        return self.width * self.height

    def display(self):
        """display rectangle"""
        for _ in range(self.y):
            print()
        for row in range(self.height):
            for i in range(self.x):
                print(" ", end="")

            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """str"""
        return(f"[Rectangle] ({self.id}) {self.x}/{self.y}- {self.width}/{self.height}")
        
    def update(self, *args, **kwargs):
        """update values"""
        if not kwargs:
            if len(args) > 5:
                raise ValueError("Too many positional arguments")

            for i, arg in enumerate(["id", "width", "height", "x", "y"]):
                if i < len(args):
                    self.int_validate(arg, args[i], arg in ("x", "y"))
                    self.__setattr__(arg, args[i])
        else:
            for attr, value in kwargs.items():
                if not hasattr(self, attr):
                    raise TypeError(f"Invalid attribute name: {attr}")
                self.int_validate(attr, value, attr in ("x", "y"))
                self.__setattr__(attr, value)
