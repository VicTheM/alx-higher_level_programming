#!/usr/bin/python3
'''
This is a supper efficient script that contains a function
to determine a max integer from a list of unsorted integers
'''

def find_peak(list_of_integers):
    ''' Finds the peak value of an unsorted list of integers.
    If the max value occur more than once, juts one instance
    is returned '''

    # The complexity of this algo is O(n)
    # But will be improved to O(log(n)) later

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
