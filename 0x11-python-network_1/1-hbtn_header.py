#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL
displays the value of the X-Request-Id variable 
"""


from urllib import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(resp.headers['X-Request-Id'])
