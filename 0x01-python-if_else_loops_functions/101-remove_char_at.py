#!/usr/bin/python3
def remove_char_at(str_, n):
    if (n < 0 or n > len(str_)):
        return (str_)
    new = str_[:n]
    new += str_[n + 1:]
    return (new)
