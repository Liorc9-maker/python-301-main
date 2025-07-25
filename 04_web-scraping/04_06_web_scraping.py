# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.
import requests
from bs4 import BeautifulSoup

# 1. Save the HTML content to a file
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

if response.status_code == 200:
    with open("python_wiki.html", "w", encoding="utf-8") as file:
        file.write(response.text)
else:
    print("Failed to retrieve the page")


# 2. Open and parse the saved HTML file
with open("python_wiki.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# 3. Extract text from the main content div
content_div = soup.find("div", {"id": "bodyContent"})
text_content = content_div.get_text(strip=True) if content_div else "No content found."

# 4. Save parsed text to a .txt file
with open("parsed_content.txt", "w", encoding="utf-8") as file:
    file.write("Article URL: " + url + "\n\n")
    file.write(text_content)
