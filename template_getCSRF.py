#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup

def getCSRF(s, url, endpoint): 

    # Getting CSRF Token
    r = s.get(url + endpoint)
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']
    print(f"[INFO] Getting CSRF Token: {csrf}")

    return csrf
