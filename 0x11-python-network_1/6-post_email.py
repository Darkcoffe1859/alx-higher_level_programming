#!/usr/bin/python3
"""
A python script that takes in a URL and an email address
sends a POST request to the url with the email as parameter
displays the body of the response
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    r = request.post(url, data=value)
    print(r.text)
