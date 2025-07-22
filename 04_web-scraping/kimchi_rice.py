import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text, features="html.parser")
#print(soup.prettify())
print()
title = soup.find("h1")
author = soup.find("p", class_="author")
recipe = soup.find("body")
print(title.text)
print(author.text)
print(recipe.text)