#!/usr/bin/python3
'''
Send a request to a URL and display the body of the response
'''

import sys
import requests


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    respon = requests.get(sys.argv[1])

    if respon.status_code >= 400:
        print('Error code:', respon.status_code)
    else:
        print(respon.text)
