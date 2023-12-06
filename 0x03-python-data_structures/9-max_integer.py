#!/usr/bin/python3

def max_integer(my_list=[]):
    len_ = len(my_list)
    if len_ == 0:
        return None

    maxx = 0
    for x in my_list:
        if x > maxx:
            maxx = x

    return maxx
