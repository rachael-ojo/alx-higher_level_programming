#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
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

    def to_dictionary(self):
        """
        Return the dictionary representation of a rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
