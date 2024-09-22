#!/usr/bin/python3
"""Defines a Retangle class"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes an instance of Rectangle

        Args:
            width (int): width of the Rectangle
            height (int): height of Rectangle
        """
        self.height = height
        self.width = width

        type(self).number_of_instances += 1

    @property
    def height(self):
        """Gets/Sets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Gets/Sets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            rect += "\n" if i + 1 < self.__height else ""
        return rect

    def __repr__(self):
        """Returns the official string representation of the Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Performs cleanup actions before the Rectangle is destroyed"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
