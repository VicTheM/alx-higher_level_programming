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

    if len(list_of_integers) == 0:
        return None

    maxx = 0
    for num in list_of_integers:
        if num > maxx:
            maxx = num

    return maxx
