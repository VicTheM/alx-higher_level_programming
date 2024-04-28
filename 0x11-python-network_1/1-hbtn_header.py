#!/usr/bin/python3
"""Sends a request to the command line url specified and prints
the 'X-Request-ID' header attribute."""

import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        responseDict = response.headers
        if 'X-Request-Id' in responseDict:
            print(responseDict['X-Request-Id'])