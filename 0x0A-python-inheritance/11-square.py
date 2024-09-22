#!/usr/bin/python3
"""Defines a Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes the Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
