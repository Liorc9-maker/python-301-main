class AgeBelowZeroError(Exception): pass

try:   
    age = int(input("Age: "))
    if age < 0:
        raise AgeBelowZeroError()
except ValueError:
    print("Please enter a numeric value.")
except AgeBelowZeroError:
    print("Looks like you've not been born yet.")
else:
    print(f"Congratulations, you're {age} years old!")
