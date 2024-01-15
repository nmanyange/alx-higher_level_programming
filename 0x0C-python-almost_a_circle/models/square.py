#!/usr/bin/python3
"""Module for a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the square

        Args:
            size(int): Size of the square
            x(int): x cordinates of the square
            y(int): y cordinates of the square
            id(int): id of the square
        Raises:
            TypeError: If size, x, y, or id is not an integer
            ValueError: If size <= 0
            ValueError: If x or y < 0
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates the square's attributes using either non-keyword
        or keyword arguments

        Args:
            *args: a tuple of arguments in the order of id, size, x, y
            **kwargs: A dictionary of keyword arguments for attributes
        """

        if args:
            # Use non-keyword arguments if provided
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            # Use keyword arguments if provided and *args is empty
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
