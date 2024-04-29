#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL
displays the value of the X-Request-Id variable
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id', None))
