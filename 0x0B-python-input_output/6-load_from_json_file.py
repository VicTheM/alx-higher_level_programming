#!/usr/bin/python3
""" JSON """


import json


def load_from_json_file(filename):
    """
    creates an obj from a json representation
    oin a file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
