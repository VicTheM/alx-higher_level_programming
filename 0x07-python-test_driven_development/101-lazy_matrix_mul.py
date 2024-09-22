#!/usr/bin/python3
"""Defines a matrix multiplication functions"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrix

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        result (numpy.array): `m_a` x `m_b`
    """
    return np.matmul(m_a, m_b)
