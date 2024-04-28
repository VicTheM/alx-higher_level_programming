#!/usr/bin/python3
"""
This is a supper efficient script that contains a function
to determine a peak integer from a list of unsorted integers
"""

def find_peak(list_of_integers):
    """ Finds the peak value of an unsorted list of integers.
    A peak is a number that is > than its neigbours
    If more than one peak occurs, we return the rightmost one """

    # Time complexity O(log(n))

    n = len(list_of_integers)
    mid = n // 2
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
