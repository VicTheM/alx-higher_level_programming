#!/usr/bin/python3
"""EMPTY CLASS"""


class Square:
    """Empty class"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """size getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            row, col = 0, 0
            while row < self.__size:
                while col < self.__size:
                    print("#", end="")
                    col += 1
                print("")
                col = 0
                row += 1
