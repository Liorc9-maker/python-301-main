# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".
from pathlib import Path

class PrinceException(Exception):
    """Custom exception raised when 'Prince' is found in the first 100 characters of a book."""
    def __init__(self, message):
        super().__init__(message)   
        self.message = message
    def __str__(self):
        return f"PrinceException: {self.message}"
    

opened_books = []
book_files = [
    Path('books/war_and_peace.txt'),
    Path('books/crime_and_punishment.txt'),
    Path('books/pride_and_prejudice.txt')
    ]

for filepath in book_files:
    try:
        with filepath.open('r', encoding='utf-8') as file:
            content = file.read(100)  # Read the first 100 characters
            if 'Prince' in content:
                raise PrinceException(f"'Prince' found in {filepath.name}")
            opened_books.append((filepath.name, content))

    except FileNotFoundError:
        print(f"{filepath.name}: File not found.")
    except PrinceException as pe:
        print(pe)
    except Exception as e:
        print(f"{filepath.name}: Error - {e}")

print("\nSuccessfully opened books (no 'Prince' found):")
for name, content in opened_books:
    print(f"- {name}")