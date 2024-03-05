#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    """
    prints x element of a list of any type

    mylist: the list as buffer
    x: number of element to print
    """
    j = -1;
    for counter in range(x):
        print("counter is : {:d}".format(counter))
        j += 1
        try:
            print("{}".format(my_list[counter]), end="")
        except Exception:
            return j

    return j
