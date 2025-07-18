# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def __str__(self):
        return f"📚 Book: '{self.title}' by {self.author} | {self.pages} pages | Genre: {self.genre}"


class Backpack:
    def __init__(self, color, size, contents):
        self.color = color
        self.size = size
        self.contents = contents  # List of items

    def __str__(self):
        return f"🎒 Backpack ({self.color}, {self.size}) with contents: {', '.join(self.contents)}"

    def __add__(self, other):
        # Combine contents of two backpacks into a new one
        combined_contents = self.contents + other.contents
        return Backpack("Mixed", "Large", combined_contents)


class WaterBottle:
    def __init__(self, brand, capacity_ml, is_insulated):
        self.brand = brand
        self.capacity_ml = capacity_ml
        self.is_insulated = is_insulated

    def __str__(self):
        insulation = "Insulated" if self.is_insulated else "Not Insulated"
        return f"🥤 {self.brand} Bottle | {self.capacity_ml}ml | {insulation}"


# --- Creating Instances ---
book1 = Book("The Alchemist", "Paulo Coelho", 208, "Fiction")
book2 = Book("Sapiens", "Yuval Noah Harari", 443, "History")

backpack1 = Backpack("Blue", "Medium", ["Notebook", "Pen", "Charger"])
backpack2 = Backpack("Black", "Small", ["Snacks", "Sunglasses"])

bottle1 = WaterBottle("HydroFlask", 750, True)
bottle2 = WaterBottle("Generic", 500, False)

# --- Print Initial State ---
print(book1)
print(book2)
print()
print(backpack1)
print(backpack2)
print()
print(bottle1)
print(bottle2)
print()

# --- Modify Attributes ---
book1.pages = 210
backpack2.contents.append("Headphones")
bottle2.is_insulated = True

# --- Print Updated State ---
print("After Modifications:\n")
print(book1)
print(backpack2)
print(bottle2)
print()

# --- Use Overloaded + Operator ---
combined_backpack = backpack1 + backpack2
print("Combined Backpack:")
print(combined_backpack)