#!/usr/bin/python3
"""Defines a matrix multiplication functions"""


def matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrix(list of lists)

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        result (list): `m_a` x `m_b`

    Raises:
        TypeError: If `m_a` or `m_b` is not a list
        TypeError: If `m_a` or `m_b` is not a list of list
        ValueError: If `m_a` or `m_b` is empty
        TypeError: If `m_a` or `m_b` doesn't contain all int or float
        TypeError: If lists within `m_a` or `m_b` are not the same size
        ValueError: If matrix multiplication is not possible
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(type(val) in [int, float] for row in m_a for val in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(val) in [int, float] for row in m_b for val in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    row_a, col_a = len(m_a), len(m_a[0])
    row_b, col_b = len(m_b), len(m_b[0])

    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for j in range(col_b)] for i in range(row_a)]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
