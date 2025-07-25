import requests
from bs4 import BeautifulSoup


BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)
soup = BeautifulSoup(page.text)
#print(page.text)
#print(type(page.text))  # OUTPUT: <class 'str'>
links = soup.find_all("a")

for link in links:
    print(link["href"])



