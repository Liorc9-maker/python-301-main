class AgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"You'll be born in {abs(self.age)} years."


age = int(input("Age: "))

try:
    if age < 0:
        raise AgeError(age)
except AgeError as ae:
    print(ae.message)
