#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for key in keys:
        print(key, end="")
        print(": {}".format(a_dictionary[key]))
