#!/usr/bin/python3
"""This script receives two command line parameters:
    1] github username
    2] Personal Access Token that has a read:user permission
    Then it prints out the user's ID using github API
    """

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    pat = sys.argv[2]
    url = 'https://api.github.com/user'

    # Test code to get a user
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + pat
            }
    req = requests.get(url, headers=headers)

    if "id" in req.json():
        user_id = req.json()["id"]
        print(user_id)
    else:
        print(None)
