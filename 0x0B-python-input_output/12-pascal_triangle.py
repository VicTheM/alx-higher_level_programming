#!/usr/bin/python3
""" TECHNICAL INTERVIEW PREP """

def pascal_triangle(n):
    """
    Creates a pascal triangle using lists
    """
    if n <= 0:
        return []

    lists = [[] for i in range(1, n + 1)]
    for row in range(1, n + 1):
        if row == 1:
            lists[0].append(1)
        else:
            length = len(lists[row - 2])

            lists[row - 1].append(1)
            for idx, itm in enumerate(lists[row - 2]):
                if idx + 1 < length:
                    lists[row - 1].append(itm + lists[row - 2][idx + 1])
            # lists[row - 1].extend([(item + lists[row - 2][index + 1]) for index, item in enumerate(lists[row - 2][1:-1])])
            lists[row - 1].append(lists[row - 2][-1])

    return lists

