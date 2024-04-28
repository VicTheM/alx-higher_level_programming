#!/usr/bin/python3
"""Make a HTTP request and prints the status code if either a client or server
error occurs"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
