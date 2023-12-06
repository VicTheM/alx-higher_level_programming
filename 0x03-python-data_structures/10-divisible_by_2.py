#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    table = [True if ele % 2 == 0 else False for ele in my_list]
    return table
