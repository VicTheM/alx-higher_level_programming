#!/usr/bin/python3
"""Contains a single function
    add_integer: adds integers and floats
    return; integer of summation
    """

def add_integer(a, b=98):
    """
    adds two integer or float

    a -- first Input
    b -- second input, default value is 98
    return: an integer
    """
    try:
        jj = 'a'
        a = int(a)
        jj = 'b'
        b = int(b)

        x = (a + b)
    except Exception:
        raise TypeError("{} must be an integer".format(jj))
    else:
        return int(x)
