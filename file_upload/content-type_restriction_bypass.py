#!/usr/bin/python3

# Attack Flow

import requests
from bs4 import BeautifulSoup
import sys

class WebRequest():

    def __init__(self, session, url, endpoint_login):
        self.session = session
        self.url = url
        self.endpoint_login = endpoint_login

    def getCSRF(session, url, endpoint_login): 
        r = session.get(url + endpoint_login)
        p = BeautifulSoup(r.content, "lxml")

        csrf = p.find(attrs = {'name' : 'csrf'})['value']
        print(f"[INFO] CSRF Token: {csrf}")

        return csrf

    def login(csrf, session, username, password, url, endpoint_login):

        data = {
            'csrf': csrf,
            'username': username,
            'password': password,
        }

        r = session.post(url + endpoint_login, data=data)
        
        if r.status_code == 200:
            p = BeautifulSoup(r.content, "html.parser")
            try:
                session_token = requests.utils.dict_from_cookiejar(session.cookies)['session']
                print(f"[INFO] Session Token: {session_token}")
            except:
                sys.exit(1)

        return session_token

def main():
    username = 'wiener'
    password = 'peter'
    url = 'https://ac291fb61fc4a0bbc00e2701006000e2.web-security-academy.net'
    endpoint_login = '/login'
    endpoint_avatar = '/my-account/avatar'

    session = requests.Session()

    csrf = WebRequest.getCSRF(session, url, endpoint_login)
    session_token = WebRequest.login(csrf, session, username, password, url, endpoint_login)


if __name__ == '__main__':
    main()
