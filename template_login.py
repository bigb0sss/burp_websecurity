import requests 
from bs4 import BeautifulSoup

# Login
def lab_login(url):

    # Getting CSRF Token
    s = requests.Session()
    r = s.get(url + "/login")
    p = BeautifulSoup(r.content, "lxml")

    csrf = p.find(attrs = {'name' : 'csrf'})['value']

    data = {
        "csrf": csrf,
        "username": "wiener",
        "password": "peter"
    }

    r = s.post(url + "/login", data=data)

    return s.cookies.get_dict()

if __name__ == '__main__':
    url = ""
