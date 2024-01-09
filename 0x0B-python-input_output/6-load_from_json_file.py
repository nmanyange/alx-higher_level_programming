#!/usr/bin/python3
"""Defines a JSON file-reading function"""


import json


def save_to_json_file(my_obj, filename):
    """Create a Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
