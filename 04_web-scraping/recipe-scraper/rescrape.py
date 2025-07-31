# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.
import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes"

class Ingredient:
    def __init__(self, name):
        self.name = name.lower()

def get_ingredients():
    ingredients_list = []
    while True:
        name = input("Enter an ingredient (or 'f' to finish): ").strip()
        if name.lower() == 'f':
            break
        if name:
            ingredients_list.append(Ingredient(name))
    return ingredients_list

def fetch_recipes(ingredients_list):
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")

        print("\nRecipes matching your ingredients (in the title):\n" + "-"*40)
        found_any = False
        for link in links:
            title = link.get_text().strip().lower()
            if any(ing.name in title for ing in ingredients_list):
                print(f"- {link.get_text().strip()}")
                print(f"  URL: {URL}/{link['href']}")
                found_any = True

        if not found_any:
            print("No matching recipes found.")
    else:
        print("Failed to fetch the recipe page.")

def main():
    print("🍽️ Welcome to the Simple Recipe Finder!")
    ingredients = get_ingredients()
    if ingredients:
        fetch_recipes(ingredients)
    else:
        print("No ingredients entered.")
    print("👋 Done!")


main()

