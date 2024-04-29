#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    req = requests.post(url, data)
    print(req.text)
