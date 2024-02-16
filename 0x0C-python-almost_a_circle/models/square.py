#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square instance.
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        """
