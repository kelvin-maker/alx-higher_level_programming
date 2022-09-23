#!/usr/bin/python3
"""
makes request and prints page infomation out
"""
from urllib.request import urlopen
if __name__ == '__main__':

    with urlopen('https://intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body Response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:" body.decode())
