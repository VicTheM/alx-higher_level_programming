#!/usr/bin/python3
""" Append text after a string in a file """


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
        containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The text to search for within the file.
        new_string (str): The text to insert if `search_string` is found.
    """
    with open(filename, encoding="utf-8") as fp:
        lines = fp.readlines()

    updated_lines = []
    for line in lines:
        updated_lines.append(line)
        if search_string in line:
            updated_lines.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as fp:
        fp.writelines(updated_lines)
