#!/usr/bin/python3
"""Define a Rectangle model"""
from models.base import Base

class Rectangle(Base):
    """Represent a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This value determines the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This value determines the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This value determine the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This value determine the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This value determine the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the '#' character"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the Rectangle"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
