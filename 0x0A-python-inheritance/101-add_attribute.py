#!/usr/bin/python3
"""Defines a add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """Adds attribute to an object

    Args:
        obj (any): The object
        attr_name (str): Attribute_name
        attr_value (any): Attribute_value

    Raises:
        TypeError: If the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
