#!/usr/bin/python3
"""Defines a LockedClass"""


class LockedClass:
    """Represents a locked class

    Attributes:
        __slots__ : restrict the class to have allowed attribute,
    """
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        """Sets the allowed attribute of the LockedClass

        Args:
            name (str): name of the attribute
            value (any): value of the attribute
        """
        if not hasattr(self, name) and name != 'first_name':
            msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(msg)
        super().__setattr__(name, value)
