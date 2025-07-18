# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, size, surface_temperature, daytime_temperature, night_temperature):
        self.name = name
        self.size = size
        self.surface_temperature = surface_temperature
        self.daytime_temperature = daytime_temperature
        self.night_temperature = night_temperature
    def __repr__(self):
        return (f"Planet name: {self.name}\n"
                f"Size: {self.size}\n"
                f"Average surface temperature: {self.surface_temperature}°C\n"
                f"Daytime temperature: {self.daytime_temperature}°C\n"
                f"Nighttime temperature: {self.night_temperature}°C")
    

mercury = Planet("Mercury", "4,880 kilometers", 167, 430, -180)
print(mercury)
print()
jupiter = Planet("Jupiter", " 142,984 kilometers", -110, -145, -110)
print(jupiter)