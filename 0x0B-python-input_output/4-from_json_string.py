#!/usr/bin/python3
""" JSON """

import json

def from_json_string(my_str):
    """
    Returns python objects
    from a JSON string
    """
    return json.loads(my_str)
