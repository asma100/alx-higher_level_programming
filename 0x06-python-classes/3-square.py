#!/usr/bin/python3

"""Square module"""


class Square:
    def __init__(self, size=0):
        """Initializes a Square object with the specified size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """

        self.__size = size

        if not isinstance(size, int) or size < 0:
            raise TypeError("size must be a non-negative integer")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
