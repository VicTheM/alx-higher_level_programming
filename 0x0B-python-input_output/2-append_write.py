#!/usr/bin/python3
""" Appends to text utf-8 file """

def append_write(filename="", text=""):
    """ Appends text to EOF """
    
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
