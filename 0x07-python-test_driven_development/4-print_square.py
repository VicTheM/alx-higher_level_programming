#!/usr/bin/python3
"""Defines a print sqaure funtion"""


def print_square(size):
    """Prints a square

    Args:
        size (int): size of square

    Raises:
        TypeError: If size is not an integer
        ValueError: If integer is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
