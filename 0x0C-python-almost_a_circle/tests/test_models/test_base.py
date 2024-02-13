#!/usr/bin/python3
import json

class Base:
    @classmethod
    def load_from_file(cls):
        """
        Deserialize objects from JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_data = file.read()
                objects_data = cls.from_json_string(json_data)

                module_name = f"models.{cls.__name__.lower()}"
                module = __import__(module_name, fromlist=[cls.__name__])
                Class = getattr(module, cls.__name__)

                instances = [Class.create(**obj) for obj in objects_data]
                return instances
        except FileNotFoundError:
            return []
