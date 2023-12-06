#!/usr/bin/python3

def check(tup):
    length = len(tup)
	if length >= 2:
		return tup
    if length == 1:
        return (tup[0], 0)
    else:
        return (0, 0)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check(tuple_a)
    tuple_b = check(tuple_b)
    one = tuple_a[0] + tuple_b[0]
    two = tuple_a[1] + tuple_b[1]

    return (one, two)



