import unittest
import rescrape


class TestRescrape(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.url = f"{self.BASE_URL}recipes/11-making-my-own-baguet.html"

    
    def test_get_valid_html_response(self):
        index_page = rescrape.get_page_content(self.BASE_URL)
        page = rescrape.get_page_content(self.url)
        self.assertEqual(index_page.status_code, 200)
        self.assertEqual(page.status_code, 200)

    def test_get_html_content_returns_html_string(self):
        index_html = rescrape.get_html_content(self.BASE_URL)
        html = rescrape.get_html_content(self.url)
        self.assertIn("<!DOCTYPE html>", index_html)
        self.assertIn("<!DOCTYPE html>", html)  

    def test_make_soup_makes_soup(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))      

    def test_get_recipe_links_gets_recipe_links(self):
        index_html = rescrape.get_html_content(self.BASE_URL)
        index_soup = rescrape.make_soup(index_html)
        self.assertGreater(len(rescrape.get_recipe_links(index_soup)), 0)

    def test_get_recipe_gets_recipe_text(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        recipe = rescrape.get_recipe(soup)
        self.assertIsInstance(recipe, str)
        self.assertGreater(len(recipe), 0)
                
if __name__ == "__main__":
    unittest.main()
