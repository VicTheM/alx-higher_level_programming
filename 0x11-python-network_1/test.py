#!/usr/bin/python3
"""Testing dictionary stuff"""

mydict = {"name": 'Victory', "age": 22}

if "name" in mydict:
    print("found name")
if 'Victory' in mydict:
    print("found value")

# The result of my test is that the 'if "x" in dict'
# searches for only keeys in dict and not values
