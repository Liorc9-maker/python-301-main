# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.
file_name = 'integers.txt'

# Attempt to read the first number from the file and perform a calculation
try:
    with open(file_name, 'r') as file:
        first_line = file.readline().strip()
        first_number = int(first_line)
except IOError:
    print(f"Error: Could not read the file '{file_name}'. Please check if the file exists and is accessible.")
except ValueError:
    print(f"Error: The first line of the file '{file_name}' is not a valid integer. Please check the file content.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    result = first_number * 2  # Example calculation
    print(f"The result of the calculation is: {result}")
