#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL
"""


from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
