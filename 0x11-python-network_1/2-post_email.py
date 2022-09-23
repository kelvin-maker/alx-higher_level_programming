#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
from urllib.parse import urlencode
from urllib.request import urlopen


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    data = urlencode({'email': sys.argv[2]}).encode()

    with urlopen(sys.argv[1], data=data) as r:
        print(r.read().decode())
