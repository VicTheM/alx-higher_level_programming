#!/usr/bin/python3
"""Posts an email to a server with the email address as parameter."""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {
        "email": email
    }

    res = requets.post(url, data=values)
    # print(res.text)
    print("Your email is: {}".format(email))
