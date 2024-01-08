#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints my name

    Args:
        first_name: Must be a string
        last_name: Must be a string

    Raises:
        TypeError: If either first_name or last_name is not a string

    Returns:
        My name is <first_name> <last_name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
