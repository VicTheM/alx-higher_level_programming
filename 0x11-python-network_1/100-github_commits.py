#!/usr/bin/python3
"""This script receives two command line parameters:
    1] name of github repo
    2] owner of the repo
    Then it prints out the 10 last commits made to the repo
    and their respective committers.
    """

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'

    # Test code to get a user
    headers = {
            "Accept": "application/vnd.github+json",
            "owner": owner,
            "repo": repo
            }
    req = requests.get(url, headers=headers)
    line_no = 1

    # Iterate through the list
    for data in req.json():
        print("{}: {}".format(data["sha"], data["commit"]["author"]["name"]))
        if line_no == 10:
            break
        line_no += 1
