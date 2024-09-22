#!/usr/bin/python3
"""Define a MyList class"""


class MyList(list):
    """Represents a list"""

    def __init(self):
        """Initializes the class"""
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
