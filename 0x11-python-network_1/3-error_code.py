#!/usr/bin/python3
"""Handles http errors"""

import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response = response.read()
            print(response.encode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))