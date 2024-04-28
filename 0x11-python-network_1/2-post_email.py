#!/usr/bin/python3
"""Posts an email to a server with the email address as parameter."""

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    datum = urllib.parse.urlencode(values)
    datum = datum.encode("ascii")

    req = urllib.request.Request(url, datum)
    with urllib.request.urlopen(req) as response:
        response = response.read()
        print(response.decode('utf-8'))
