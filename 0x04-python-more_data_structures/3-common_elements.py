#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns common elements"""

    set_3 = set([x for x, y in zip(set_1, set_2) if x == y])
    return set_3
