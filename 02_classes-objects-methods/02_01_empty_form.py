# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Dog:
    def __init__(self, name, breed, is_cute, is_naughty):
        self.name = name
        self.breed = breed
        self.is_cute = is_cute
        self.is_naughty = is_naughty
        print(self)

    def __str__(self):
        return(f"Dog name is: {self.name}\n"
              f"Breed is: {self.breed}\n"
              f"Is cute: {self.is_cute}\n"
              f"Is naughty: {self.is_naughty}\n")


dog1 = Dog("Yogi", "Mixed breed", True, False)        
dog2 = Dog("Sweetheart","Mixed breed", True, True)
dog3 = Dog("Arjun", "Mixed breed", False, True)
dog4 = Dog("Luna", "Dutch shepherd", True, False)
dog5 = Dog("Shakti", "Labrador", True, False)
dog6 = Dog("Mama sun", "Mixed breed", False, False)

