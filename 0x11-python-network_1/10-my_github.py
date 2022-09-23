#!/usr/bin/python3
'''
Log in to Github
'''

import sys
import requests

URL = 'https://api.github.com/user'

if __name__ == '__main__':
    auth = (sys.argv[1], sys.argv[2])
    resp = requests.get(URL, auth=auth)
    data = resp.json()
    print(data.get('id'))
