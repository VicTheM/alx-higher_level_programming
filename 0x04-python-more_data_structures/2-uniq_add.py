#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = my_list[:]

    result = list(set(new_list))

    result_2 = 0
    for num in result:
        result_2 += num
    return result_2
