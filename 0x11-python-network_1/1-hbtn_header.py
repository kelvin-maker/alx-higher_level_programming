#!/usr/bin/python3
'''
Makes a request to a URL and displays the value of the X-Request-Id header
'''
import sys
from urllib.request import

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ", __file__, "URL", file=sys.stderr)
        sys.exit(2)

    with urlopen(sys.argv[1]) as respon:
        print(respon.getheader("X-Request-Id"))
        
