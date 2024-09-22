#!/usr/bin/python3
"""Defines a Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes the Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
