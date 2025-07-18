# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius =radius
    def area(self):
        return  pi * self.radius ** 2
    
    def circumference(self):   
        return pi * self.radius * 2

    def __repr__(self):
        return(f"Circle area is: {self.area()}\n"
               f"Circle circumference is {self.circumference()}")

cir1 = Circle(3)
print(cir1)            


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __repr__(self):
        return(f"Rectangle's area is {self.area()}\n"
               f"Rectangle's perimeter is {self.perimeter()}")    


rec1 = (Rectangle(7,3))
print(rec1)    