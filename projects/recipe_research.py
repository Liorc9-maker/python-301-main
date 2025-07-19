# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.
import webbrowser


class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def combine(self,other):
        combined_name = f"{self.name}-{other.name}"
        combined_amount = self.amount + other.amount
        print(f"You now have {combined_amount} of {combined_name}.")
        return Spice(combined_name, combined_amount)
      
    def expire(self):
        if self.name == "salt":
            print(f"Salt never expires, ask the sea!")
        else:
            print(f"your {self.name} has expired. it's probably still good.")
            self.name = "old " + self.name 

class Soup:
    """Takes a list of ingredients and searches for a soup recipe online."""

    def __init__(self, ingredients):  
        self.ingredients = ingredients

    def cook(self):
        names = [ingredient.name for ingredient in self.ingredients]
        query = "+".join(names) + "+soup+recipe"
        url = f"https://www.google.com/search?q={query}"
        print(f"Searching: {url}")
        webbrowser.open_new(url)

import webbrowser

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"{self.amount} of {self.name}"


class Spice(Ingredient):
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def combine(self, other):
        combined_name = f"{self.name}-{other.name}"
        combined_amount = self.amount + other.amount
        print(f"You now have {combined_amount} of {combined_name}.")
        return Spice(combined_name, combined_amount)

    def expire(self):
        if self.name.lower() == "salt":
            print("Salt never expires, ask the sea!")
        else:
            print(f"Your {self.name} has expired. It's probably still good.")
            self.name = "old " + self.name


class Soup:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def cook(self):
        names = [ingredient.name for ingredient in self.ingredients]
        query = "+".join(names) + "+soup+recipe"
        url = f"https://www.google.com/search?q={query}"
        print(f"Searching: {url}")
        webbrowser.open_new(url)


# === Interactive Program ===

ingredients = []
spices = []

def main():
    print("🍲 Welcome to Soup Builder 3000!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Create Ingredient")
        print("2. Create Spice")
        print("3. View Created Items")
        print("4. Make and Cook Soup")
        print("5. Exit")
        choice = input("Enter choice (1–5): ")

        if choice == "1":
            name = input("Ingredient name: ")
            amount = input("Amount: ")
            ingredients.append(Ingredient(name, amount))
            print(f"✅ Added ingredient: {name}")

        elif choice == "2":
            name = input("Spice name: ")
            amount = input("Amount: ")
            taste = input("Taste (e.g., spicy, sweet): ")
            spices.append(Spice(name, amount, taste))
            print(f"✅ Added spice: {name}")

        elif choice == "3":
            print("\n🧾 Your Ingredients:")
            for i, ing in enumerate(ingredients, 1):
                print(f"{i}. {ing}")
            print("\n🧂 Your Spices:")
            for i, sp in enumerate(spices, 1):
                print(f"{i}. {sp}")

        elif choice == "4":
            if not ingredients and not spices:
                print("❗ You need to create ingredients or spices first!")
                continue
            print("\nSelect items to add to your soup (comma-separated indices):")
            all_items = ingredients + spices
            for i, item in enumerate(all_items, 1):
                print(f"{i}. {item}")
            selected = input("Your selection: ")
            try:
                indices = [int(i.strip()) - 1 for i in selected.split(",")]
                selected_items = [all_items[i] for i in indices if 0 <= i < len(all_items)]
                soup = Soup(selected_items)
                soup.cook()
            except Exception as e:
                print(f"⚠️ Invalid input: {e}")

        elif choice == "5":
            print("👋 Goodbye, happy soup-making!")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
