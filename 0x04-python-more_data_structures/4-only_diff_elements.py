#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns common elements"""

    # set_3 = set([x for x in set_1 if x not in set_2])

    set_3 = set_1.union(set_2)
    return set_3
