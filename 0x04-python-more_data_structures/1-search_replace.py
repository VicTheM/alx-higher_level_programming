#!/usr/bin/env python3
# #!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces @search with @replace in @my_list"""
    # c = 0
    new_list = my_list[:]
    for index, item in enumerate(my_list):
        if item == search:
            new_list[index] = replace
        # c += 1

    return new_list
