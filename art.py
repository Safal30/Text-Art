import requests
from bs4 import BeautifulSoup

print(F'''                                        
 -safal30
''')

text = input("Keyword: ")

url = "http://artii.herokuapp.com/make?text="
new_url = (url + text)


url_req = requests.get(new_url)
url_text = url_req.text
url_code = url_req.status_code

def fetch(saf):
    if url_code == 200:
        url_bs = BeautifulSoup(url_text, "html.parser")
        print(url_bs)
    else:
        print("Unexpected error") 
fetch(url_text)
