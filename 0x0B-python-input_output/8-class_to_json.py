#!/usr/bin/python3
""" Custom JSON Serializer """


import json


def class_to_json(obj):
    """
    Returns the dict representation of obj
    so it can be serialized by json

    NOTE: all attributes of obj must be
    inherently serializable
    """
    return obj.__dict__
