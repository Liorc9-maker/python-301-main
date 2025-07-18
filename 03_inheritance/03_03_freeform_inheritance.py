# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model} engine starts with a roar!")

    def __str__(self):
        return(f"{self.year} {self.make} {self.model}")


class Truck(Vehicle):
    def __init__(self, make, model, year, bed_length):
        super().__init__(make, model, year)            
        self.bed_length = bed_length

    def haul(self):
        print(f"The truck with a {self.bed_length}-foot bed is hauling materials.")

    def __str__(self):
        return super().__str__() + f" | Bed Length: {self.bed_length} ft"    

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_cc):
        super().__init__(make, model, year)
        self.engine_cc = engine_cc

    def do_wheelie(self):
        print(f"The {self.make} motorcycle with an engine of {self.engine_cc} cc pops a wheelie!")            

    def __str__(self):
        return super().__str__() + f" | Engine: {self.engine_cc}cc"    
    
class ElectricTruck(Truck):
    def __init__(self, make, model, year, bed_length, battery_range):
        super().__init__(make, model, year, bed_length)    
        self.battery_range = battery_range

    def charge(self):
        print(f"The electric truck is charging. Range: {self.battery_range} miles.")    

    def __str__(self):
        return super().__str__() + f" | Battery Range: {self.battery_range} mi"


# Base
v = Vehicle("Toyota", "Corolla", 2020)
print(v)
v.start_engine()
print()
# Child
t = Truck("Ford", "F-150", 2022, 6.5)
print(t)
t.haul()
print()
# Another child
m = Motorcycle("Yamaha", "R3", 2021, 321)
print(m)
m.do_wheelie()
print()
# Grandchild
et = ElectricTruck("Tesla", "Cybertruck", 2024, 6, 500)
print(et)
et.charge()
