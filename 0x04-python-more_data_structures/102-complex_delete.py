#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete_keys = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val == value:
                to_delete_keys.append(key)
        for key in to_delete_keys:
            del a_dictionary[key]
    return a_dictionary
