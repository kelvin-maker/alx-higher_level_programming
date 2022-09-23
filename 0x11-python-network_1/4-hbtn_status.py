#!/usr/bin/python3
'''
Send a request to a URL and display the body of the response
'''

import requests

URL = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':

    respon = requests.get(URL)
    print("Body response:")
    print("\t- type:", type(respon.text))
    print("\t- content:", respon.text)
    
