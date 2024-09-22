#!/usr/bin/python3

"""Computers the addition of two integers
Calls the function add_intger(a, b)
Args:
    a (int): first integer
    b (:obj:`int`, optional): second integer """


def add_integer(a, b=98):
    """Returns the addition of two integers
    Returns:
        The sum of `a` and ``b`` """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
