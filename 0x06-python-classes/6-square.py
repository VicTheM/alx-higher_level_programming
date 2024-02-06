#!/usr/bin/python3
"""EMPTY CLASS"""


class Square:
    """Empty class"""

    def __init__(self, size=0, dimension=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(dimension, tuple) or len(dimension) != 2 or\
                dimension[0] < 0 or dimension[1] < 0:
            raise TypeError("position must be a\
                    tuple of two positive integers")
        self.__position = dimension

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
        """gets area"""
        return (self.__size * self.__size)

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter"""
        if not isinstance(value, tuple) or len(value) != 2 or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple\
                    of two positive integers")
        self.__position = value

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                x = 0
                while x < self.__position[1]:
                    print("")
                    x += 1
            x = self.__position[0]
            row, col = 0, 0
            while row < self.__size:
                j = 0
                while j < x:
                    print("", end=" ")
                    j += 1
                while col < self.__size:
                    print("#", end="")
                    col += 1
                print("")
                col = 0
                row += 1
