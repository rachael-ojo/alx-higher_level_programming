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

                # Dynamically import the class based on the class name
                module_name = f"models.{cls.__name__.lower()}"
                module = __import__(module_name, fromlist=[cls.__name__])
                Class = getattr(module, cls.__name__)

                # Create instances using the create method
                instances = [Class.create(**obj) for obj in objects_data]
                return instances
        except FileNotFoundError:
            return []
