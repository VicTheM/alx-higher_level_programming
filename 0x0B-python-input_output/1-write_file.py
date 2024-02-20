#!/usr/bin/python3
""" This script contains function that writes to a file """

def write_file(filename="", text=""):
    """
    writes @text into @filename
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
