#!/usr/bin/python3
'''
script that fetches https://alx-intranet.hbtn.io/status
'''


import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    resp = urllib.request.urlopen(url)
    html = resp.read()
    resp.close()
    print('Body response:')
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf8')}")
