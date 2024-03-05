#!/usr/bin/python3
""" JSON """


import json


def to_json_string(my_obj):
    """
    Returns JSON string representation of
    a serializable object
    """

    return json.dumps(my_obj)
