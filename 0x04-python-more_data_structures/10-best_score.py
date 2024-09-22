#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        person = ""
        best_score = 0
        for key, value in a_dictionary.items():
            if value > best_score or person == "":
                best_score = value
                person = key
        return person
    else:
        return None
