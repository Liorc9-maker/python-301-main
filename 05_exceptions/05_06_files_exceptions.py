# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?
from pathlib import Path

# 1. Read full content of war_and_peace.txt
try:
    with Path('books/war_and_peace.txt').open('r', encoding='utf-8') as file:
        war_and_peace_content = file.read()
except FileNotFoundError:
    war_and_peace_content = None
    print("Error: war_and_peace.txt not found.")
except Exception as e:
    war_and_peace_content = None
    print(f"Unexpected error reading war_and_peace.txt: {e}")

# 2. Overwrite crime_and_punishment.txt with an empty string
try:
    with Path('books/crime_and_punishment.txt').open('w', encoding='utf-8') as file:
        file.write('')
except FileNotFoundError:
    print("Error: crime_and_punishment.txt not found.")
except Exception as e:
    print(f"Unexpected error overwriting crime_and_punishment.txt: {e}")

# 3. Loop over all three files and print the first character
book_files = [
    Path('books/war_and_peace.txt'),
    Path('books/crime_and_punishment.txt'),
    Path('books/pride_and_prejudice.txt')
]

print("\nFirst characters from each book:")
for filepath in book_files:
    try:
        with filepath.open('r', encoding='utf-8') as file:
            first_char = file.read(1)
            if first_char:
                print(f"{filepath.name}: '{first_char}'")
            else:
                print(f"{filepath.name}: [Empty file]")
    except FileNotFoundError:
        print(f"{filepath.name}: File not found.")
    except Exception as e:
        print(f"{filepath.name}: Error - {e}")
