# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

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
class Vegetable(Ingredient):

    def choped(self):
        print(f"You now have choped {self.name}")

    def expire(self):
        print(f'Your choped {self.name} has gone bad, put it in the copost.')
        self.name = "composting " + self.name    


p = Ingredient('peas', 12)
print(p)  # OUTPUT: You have 12 peas.
s = Spice('salt', 200, "salty")
print(s)  # OUTPUT: You have 200 salt.
s.grind()

#c = Ingredient('carrots', 3)
#p = Spice('pepper', 20)

#p.grind() 
#sp = s.combine(p)
#s.expire()
#print(s)

#j = Ingredient("salt", 100)
#j.expire()
#print(j)

o = Vegetable("kale", 200)
print(o)
o.expire()
print(o)

c = Ingredient("carrots", 2)
p = Spice("pepper", 20, "hot")
print(p.taste)