#!/usr/bin/env python3


def flatten(arr=[]):
    """Flattens an array"""
    flat = [x for listt in arr for x in listt]
