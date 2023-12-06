#!/usr/bin/python3

def multiple_returns(sentence):
    len_ = len(sentence)
    if len_ == 0:
        return 0, None
    tup = (len_, sentence[0])
    return tup
