# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.
import requests
from bs4 import BeautifulSoup
class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to retrieve the page: {response.status_code}")

    def save_html_to_file(self, html_content, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)

    def load_html_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.soup = BeautifulSoup(file, "html.parser")

    def extract_text(self):
        if self.soup is None:
            raise Exception("No HTML content loaded.")
        content_div = self.soup.find("div", {"id": "bodyContent"})
        return content_div.get_text(strip=True) if content_div else "No content found."

    def save_parsed_text_to_file(self, text_content, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Article URL: " + self.url + "\n\n")
            file.write(text_content)

if __name__ == "__main__":
    oop = WebScraper("https://en.wikipedia.org/wiki/Object-oriented_programming")
    oop_html = oop.fetch_html()            
    oop.save_html_to_file(oop_html, "oop_wiki.html")
    oop.load_html_from_file("oop_wiki.html")
    oop_text = oop.extract_text()
    oop.save_parsed_text_to_file(oop_text, "oop_parsed_content.txt")
