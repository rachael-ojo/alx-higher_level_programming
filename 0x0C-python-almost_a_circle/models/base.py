#!/usr/bin/python3
"""This module contain Base class and some imported modules"""
import json
import os
import csv
import turtle

class Base:
    """The class Base for its instances
    Attributes:
        __nb_objects (int): Is the number of objects created from this class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """the initializing method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set using dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            raise TypeError(f"Unsupported class: {cls.__name__}")

        dummy.update(**dictionary)  # Update dummy instance with dictionary
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                return [cls.create(**dictionary) for dictionary in dictionaries]
        except FileNotFoundError:
            return []
