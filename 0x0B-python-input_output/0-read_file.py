#!/usr/bin/python3
""" This script contains a function that read a UTF-8 file """

def read_file(filename=""):
    """
    Reads a text file and prints the content
    """
    with open(filename, 'r') as file:
        data = file.read();
        print(data, end="");
