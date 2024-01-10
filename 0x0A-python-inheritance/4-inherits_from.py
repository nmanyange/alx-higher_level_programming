#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Check if an object is exactly an inheritef instance of a given class
    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj to
    Returns:
        If an obj is an instance or inherited instance of a_class - True
        Otherwise - False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
