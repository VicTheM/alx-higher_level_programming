#!/usr/bin/python3
"""Defines a MyInt class"""


class MyInt(int):
    """Represents an integer"""

    def __init__(self, value):
        """Initializes the integer"""
        super().__init__()

    def __eq__(self, other):
        """Defines the == comparison of MyInt"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines the != comparison of MyInt"""
        return super().__eq__(other)
