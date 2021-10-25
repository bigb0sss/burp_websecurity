#!/usr/bin/python3

import requests
import sys

def connect(url, api):

    r = requests.get(url + api)

    return


if __name__ == '__main__':
    url = ""
    api = ""

    connect(url, api)