#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    A new matrix with all elements divided by `div'

    Args:
        matrix (list): A list of lists.
            Has same size and it contains only real numbers.
        div (int/float) : Number to divide by

    Returns: `matrix` divided by `div`

    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If all rows aren't the same size
        TypeError: If div is not a real number
        ZeroDivisionError: If `div` is 0
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == [] or\
            not all(isinstance(row, list) for row in matrix) or\
            not all(type(value) in [float, int]
                    for row in matrix for value in row):
        raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((value / div), 2) for value in row] for row in matrix]
# This works as well
# list(map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix))
