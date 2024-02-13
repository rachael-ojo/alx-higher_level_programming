#!/usr/bin/python3
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
