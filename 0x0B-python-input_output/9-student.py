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

    def to_json(self):
        """Get a dictionary representation ot a student"""
        student_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
        return student_dict
