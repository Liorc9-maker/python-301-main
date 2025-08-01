# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.
import rescrape
import pytest
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"
RECIPE_URL = f"{BASE_URL}recipes/11-making-my-own-baguet.html"


def test_get_valid_html_response():
    index_page = rescrape.get_page_content(BASE_URL)
    page = rescrape.get_page_content(RECIPE_URL)
    assert index_page.status_code == 200
    assert page.status_code == 200


def test_get_html_content_returns_html_string():
    index_html = rescrape.get_html_content(BASE_URL)
    html = rescrape.get_html_content(RECIPE_URL)
    assert "<!DOCTYPE html>" in index_html
    assert "<!DOCTYPE html>" in html


def test_make_soup_makes_soup():
    html = rescrape.get_html_content(RECIPE_URL)
    soup = rescrape.make_soup(html)
    assert isinstance(soup, BeautifulSoup)


def test_get_recipe_links_gets_recipe_links():
    index_html = rescrape.get_html_content(BASE_URL)
    index_soup = rescrape.make_soup(index_html)
    links = rescrape.get_recipe_links(index_soup)
    assert len(links) > 0


def test_get_recipe_gets_recipe_text():
    html = rescrape.get_html_content(RECIPE_URL)
    soup = rescrape.make_soup(html)
    recipe = rescrape.get_recipe(soup)
    assert isinstance(recipe, str)
    assert len(recipe) > 0
