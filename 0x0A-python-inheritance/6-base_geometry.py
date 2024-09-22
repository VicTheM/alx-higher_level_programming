#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Reperesents a geometric shape"""

    def area(self):
        """Raises an exception if function is not implemented

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
