# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.

class Movie():
    def __init__(self, year, title):
        self.year = year
        self.title = title
        self.available = True
    def rent(self):
        self.available = False
        print(f"{self.title} is rented")

    def retured(self):
        self.available = True
        print(f"{self.title} is now available for rent")        

    def __str__(self):
        return(f"{self.title} | {self.year}")
    
class RomCom(Movie):
    def __init__(self, year, title):
        super().__init__(year, title)
        self.genre = "Romantic comedies"
    def __str__(self):
        return(f"{self.title} | {self.genre} | {self.year}")
class ActionMovie(Movie):
    def __init__(self, year, title):
        super().__init__(year, title)
        self.pg = 13
    def __str__(self):    
        return(f"{self.title} | {self.year} | {self.pg}")
    




# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?
a = Movie(2022, "waste collection adventures")
print(a)
b = Movie(2023, "Compost horrors")
print(b)
c = RomCom(2023, "Love on the moon")
print(c)
d = ActionMovie(2025, "Jurassic World Rebirth")
print(d)
d.rent()
d.retured()