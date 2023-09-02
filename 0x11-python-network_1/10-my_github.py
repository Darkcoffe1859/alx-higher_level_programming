#!/usr/bin/python3
"""This scripts takes my github username and password 
uses the API to display my id
"""
import sys
import requests



if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
