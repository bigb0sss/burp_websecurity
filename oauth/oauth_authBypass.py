#!/usr/bin/python3

import requests

def connect(url, endpoint):

    s = requests.Session()
    r = s.get(url + endpoint)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    url = "https://acb61f1c1ee2365cc02e0328008700eb.web-security-academy.net"
    endpoint = "/my-account"

    connect(url, endpoint)


# https://oauth-ac851f2c1e043677c037034d020e0029.web-security-academy.net/auth?client_id=n644yofrlu0ycgt9g8mde&redirect_uri=https://acb61f1c1ee2365cc02e0328008700eb.web-security-academy.net/oauth-callback&response_type=token&nonce=-170985035&scope=openid%20profile%20email