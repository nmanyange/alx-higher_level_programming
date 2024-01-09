#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a new student
        Args:
            first_name(str): The first nsmr of the student
            last_name(str): The last name of the student
            age(int): Age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation ot a student

        Args:
        attrs(list): (Optional) The attributes to represent
        """

        if attrs is None:
            return self.__dict__
        else:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    def reload_from_json(self, json):
        """Replace all attributes of the student
        Args:
            json(dict): The key/value to replace the attributes with
        """
        for k, v in json.items():
            setattr(self, k, v)
