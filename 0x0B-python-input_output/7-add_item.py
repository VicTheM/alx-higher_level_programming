#!/usr/bin/python3
"""
JSON

This script saves all the comand line arguments
passed to it in json format in a json file
"""

import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

filepath = "add_item.json"

if len(sys.argv) > 1:
    try:
        new_list = load(filepath)
        new_list.extend(sys.argv[1:])
    except FileNotFoundError:
        new_list = sys.argv[1:]
    save(new_list, filepath)
