# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.
import requests
from bs4 import BeautifulSoup
import random

URL = "https://en.wikipedia.org/wiki/Web_scraping"
page = requests.get(URL)
soup = BeautifulSoup(page.text, features="html.parser")
links = soup.find_all("a", href=True)
excluded_prefixes = ("/wiki/Special:", "/wiki/File:", "/wiki/Help:", "/wiki/Talk:", "/wiki/Category:", "/wiki/Portal:", "/wiki/Wikipedia:")
filtered_links = [link['href'] for link in links if link['href'].startswith("/wiki/") and not any(link['href'].startswith(prefix) for prefix in excluded_prefixes)]
print("Filtered Links:")
link_beginswith = "https://en.wikipedia.org"
for link in filtered_links:
    print(link_beginswith+link) 
# Follow one of the links to another Wikipedia article
if filtered_links:
    next_url = link_beginswith + random.choice(filtered_links)
    next_page = requests.get(next_url)
    next_soup = BeautifulSoup(next_page.text, features="html.parser")

    content_div = next_soup.find("div", {"id": "bodyContent"})
    text_content = content_div.get_text() if content_div else "No content found."
    
    with open("wikipedia_article.txt", "w", encoding="utf-8") as file:
        file.write(f"Article URL: {next_url}\n\n")
        file.write(text_content)     
    