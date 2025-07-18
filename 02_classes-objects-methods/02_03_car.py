# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    def __init__(self, make, model, top_speed):
      self.make = make
      self.model = model
      self.top_speed = top_speed

    def increase_speed(self):
      self.top_speed += 5
    
    def __repr__(self):
       return(f"Car make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Top speed: {self.top_speed} km/h\n")
   
ssc = Car("SSC", "Tuatara", 509)
bugatti = Car("BUGATTI", "Chiron", 490)
ford = Car("Ford", "M2K MOTORSPORTS Ford GT", 483)
print(ssc)   
ssc.increase_speed()
print(f"After increasing speed:\n{ssc}\n")
print(bugatti)
bugatti.increase_speed()
print(f"After increasing speed:\n{bugatti}\n")
print(ford)
ford.increase_speed()
print(f"After increasing speed:\n{ford}")
