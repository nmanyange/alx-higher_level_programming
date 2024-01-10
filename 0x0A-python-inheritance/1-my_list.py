#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """Represents a list class with a method to print the list sorted"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
