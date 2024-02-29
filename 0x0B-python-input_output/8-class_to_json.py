#!/usr/bin/python3
""" Custom JSON Serializer """


def class_to_json(obj):
    """
    Returns the dict representation of obj
    so it can be serialized by json

    Args:
        obj: (any)

    NOTE: all attributes of obj must be
    inherently serializable
    """
    
    return obj.__dict__
