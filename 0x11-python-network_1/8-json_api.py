#!/usr/bin/python3
"""A script that takes in a letter,
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter sent in the variable q
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    r = requests.post(url, data=data)

    try:
        r = r.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
