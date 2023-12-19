#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """"Represent a square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
           size (int): The size of a new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the currrent size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
