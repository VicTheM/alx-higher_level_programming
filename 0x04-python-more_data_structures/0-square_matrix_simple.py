#!/usr/bin/python3

def squ_them(arr=[]):
    new_arr = list(map(lambda x: x**2, arr))

    return new_arr


def square_matrix_simple(matrix=[]):
    """Squares all the element of a matrix"""

    if matrix is None:
        return None

    new_matrix = list(map(squ_them, matrix))

    return new_matrix
