#!/usr/bin/python3
""" A python script that takes two argument to solve  challenge
using the github API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}commits"\
          .format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get("commit").get("author").get("name"))
