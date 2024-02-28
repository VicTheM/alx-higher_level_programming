#!/usr/bin/env python3

def my_function(*kids):
    for arg in kids:
        print(arg)
my_function("me", "you")
my_function()
