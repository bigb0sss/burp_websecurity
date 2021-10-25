#!/usr/bin/python3

import requests
import sys

def connect(url, api):

    data = {
        "test" : "test",
    }

    r = requests.post(url + api, data = data)

    return


if __name__ == '__main__':
    url = ""
    api = ""

    connect(url, api)