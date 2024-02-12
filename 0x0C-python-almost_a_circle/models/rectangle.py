#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle representation using the character '#'.
        """
        for _ in range(self.y):
            print()
        
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Assign attributes using both positional and keyword arguments.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

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
        Return a string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
