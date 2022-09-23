#!/usr/bin/python3
'''
Take a letter and send a POST request to http://0.0.0.0:5000/search_user
'''

import sys
import requests

URL = 'http://0.0.0.0:5000/search_user'

if __name__ == '__main__':

    data = {'q': '' if len(sys.argv) == 1 else sys.argv[1]}
    respon = requests.post(URL, data=data)
    try:
        json = respon.json()
    except ValueError:
        print('Not a valid JSON')
    else:
        if json:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
