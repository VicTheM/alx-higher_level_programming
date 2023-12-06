#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        row_len = len(row)
        i = 0
        for ele in row:
            i += 1
            if i < row_len:
                print("{:d}".format(ele), end=" ")
            else:
                print("{:d}".format(ele))
