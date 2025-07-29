# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    quotient = numerator / denominator
except ValueError:
    print("Invalid input! Please enter numeric values.")    
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print(f"The quotient of {numerator} and {denominator} is {quotient}")