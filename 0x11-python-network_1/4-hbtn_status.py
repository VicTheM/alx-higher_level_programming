#!/usr/bin/python3
"""Make a HTTP request using the requests module"""

if __name__ == '__main__':
    import requests

    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
