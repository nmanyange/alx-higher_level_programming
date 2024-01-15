#!/usr/bin/python3
"""Module for Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represents a class Rectangle which inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of the rectangle.

        Args:
            width(int): The width of the rectangle
            height(int): The hright if the rectangle
            x(int): X cordinates of the rectangle
            y(int): Y cordinates of the rectangle
            id(int):The id of the rectangle
        Raises:
            TypeError: If width, height, x, y or id is not an integer
            ValueError: If width or height <= 0
            ValueError: If x or y < 0
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Getter for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter for width"""
            self.validate_int("width", value, positive=True)
            self.__width = value

        @property
        def height(self):
            """Getter for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for height"""
            self.validate_int("height", value, positive=True)
            self.__height = value

        @property
        def x(self):
            """Getter for x"""
            return self.__x

        @x.setter
        def x(self, value):
            """Setter for x"""
            self.validate_int("x", value, non_negative=True)
            self.__x = value

        @property
        def y(self):
            """Getter for y"""
            return self.__y

        @y.setter
        def y(self, value):
            """Setter for y"""
            self.validate_int("y", value, non_negative=True)
            self.__y = value

        def _validate_int(self, name, value, positive=False, non_negative=False):
            """Validates an integer value for a given attribute"""
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if positive and value <= 0:
                raise ValueError("{} must be > 0".format(name))
            if non_negative and value < 0:
                raise ValueError("{} must be >= 0".format(name))

        def area(self):
            """Calculates and returns the area of the rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """Returns a string representation of the rectangle"""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

        def display(self):
            """Displays a visual representation of the rectangle using #
            character taking into account x and y cordinates"""
            for _ in range(self.y):
                print()
            print(" " * self.x, end="")

            for _ in range(self.height):
                print("#" * self.width)

        def __update(self, id=None, width=None, height=None, x=None, y=None):
            '''Internal method that updates instance attributes via */**args.'''
            if id is not None:
                self.id = id
            if width is not None:
                self.width = width
            if height is not None:
                self.height = height
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y

        def update(self, *args, **kwargs):
            """Updates the rectangle's attributes using either non-keyword
            or keyword arguments

            Args:
                *args: a tuple of argummentsin the order of id, width,
                height, x, y
                **kwargs: A dictionary of keyword arguments for attributes
            """

            if args:
                if len(args) != 5:
                    raise TypeError("update() takes exactly 5 arguments")
                self.__update(*args)
            else:
                for key, value in kwargs.items():
                    if key in ("id", "width", "height", "x", "y"):
                        setattr(self, key, value)
                    else:
                        raise TypeError("Invalid argument: {}".format(key))

        def to_dictionary(self):
            """Returns the dictionary representation of the rectangle"""
            return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
