#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """Base class for managing id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class.

        Args:
            id(int): If not None assigns id as the public instance attribute
            otherwise, increment __nb_objects and assign the new value to the
            public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        json_str = "[]"

        if list_objs is not None:
            json_str = cls.to_json_string([o.to_dictionary() for o in list_objs])

        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries from the JSON string representation."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class for create method")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                instances = [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            pass

        return instances
