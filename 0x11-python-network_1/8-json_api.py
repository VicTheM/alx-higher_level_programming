#!/usr/bin/python3
"""This script demonstrates the simple use of an API.
It makes a request to an external application and if the
returned response is JSON formatted, it searches for the
required data in the response"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv >= 2):
        sch_str = sys.argv[1]
    else:
        sch_str = ""

    payload = {'q': sch_str}
    req = requsts.post(url, data=payload)

    try:
        if req.json == {}:
            print ("No result")
        else:
            print("[{}] {}".format(req.json()["id"], req.json["name"]))
    except ValueError:
        print("Not a valid JSON")
