#!/usr/bin/python3
"""Sends a request to the command line url specified and prints
the 'X-Request-ID' header attribute."""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    if 'X-Request-Id' in res.headers:
        print(res.headers['X-Request-Id'])
