#!/usr/bin/python3

def no_c(my_string):

    new_str = ''
    for word in my_string:
        if word not in 'cC':
            new_str = new_str + word
    # new_str = [x for x in my_string if x not in 'cC']
    return new_str
