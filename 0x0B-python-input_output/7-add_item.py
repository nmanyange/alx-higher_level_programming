#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file"""


import json
from sys import argv
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_arguments_to_list(args):
    file_name = 'add_item.json'

    # Load existing data from file or initialize an empty list
    if exists(file_name):
        data = load_from_json_file(file_name)
    else:
        data = []

    # Add arguments to the list
    data.extend(args)

    # Save the updated list to the file
    save_to_json_file(data, file_name)

if __name__ == "__main__":
    # Extract command line arguments except the script name
    arguments = argv[1:]
    add_arguments_to_list(arguments)
    print("Arguments added to 'add_item.json'")
