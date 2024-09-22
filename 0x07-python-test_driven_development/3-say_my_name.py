#!/usr/bin/python3
"""Define a function to print name"""


def say_my_name(first_name, last_name=""):
    """Print a persons first and last name

    Args:
        first_name (str): first name
        last_name (:obj:`str`, optional): last name

    Raises:
        TypeError: If first or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
