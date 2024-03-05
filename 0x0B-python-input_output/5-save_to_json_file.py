#!/usr/bin/python3
""" JSON """


import json


def save_to_json_file(my_obj, filename):
    """
    Serializes @my_obj and writes to
    @filename in json format
    """
    with open(filename, 'w', encoding="utf-8") as filename:
        json.dump(my_obj, filename)
