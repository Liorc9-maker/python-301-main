import webbrowser

class Ingredients:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        webbrowser.open_new(f"https://en.wikipedia.org/wiki/{self.name}")

    def __repr__(self):
        return f"Name {self.name} Amount {self.amount}"

# Create ingredient objects
carrot = Ingredients("carrot", 3)
pea = Ingredients("pea", 7)
orange = Ingredients("orange", 9)

print(carrot)
print(pea)
print(orange)

# Map names to objects for easy lookup
ingredients_dict = {
    "carrot": carrot,
    "pea": pea,
    "orange": orange
}

# Ask user for input
search = input("Type the ingredient name you want to search: ").lower()

# Check and call get_info if it exists
if search in ingredients_dict:
    ingredients_dict[search].get_info()
else:
    print("Sorry, ingredient not found.")