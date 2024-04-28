#!/usr/bin/python3
"""This script demonstrates the simple use of an API.
It makes a request to an external application and if the
returned response is JSON formatted, it searches for the
required data in the response"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {
            "q": "" if len(sys.argv) == 1 else sys.argv[1]
            }
    response = requests.post(url, data=data)

    try:
        json = response.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json["id"], json["name"]))
    except ValueError:
        print("Not a valid JSON")
