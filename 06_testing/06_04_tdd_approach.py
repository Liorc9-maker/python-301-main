# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest
from pathlib import Path

class TestFileOperations(unittest.TestCase):
    def test_write_to_file_creates_file(self):
        file_path = Path("test_file.txt")
        content = "Hello, World!"
        
        # Simulate writing to a file
        with open(file_path, 'w') as f:
            f.write(content)
        
        self.assertTrue(file_path.exists())
        self.assertEqual(file_path.read_text(), content)
        
        # Clean up
        file_path.unlink()

    def test_read_from_file_returns_content(self):
        file_path = Path("test_file.txt")
        content = "Hello, World!"
        
        # Create a file with content
        with open(file_path, 'w') as f:
            f.write(content)
        
        with open(file_path, 'r') as f:
            read_content = f.read()
        
        self.assertEqual(read_content, content)
        
        # Clean up
        file_path.unlink()

    def test_file_not_found_raises_error(self):
        file_path = Path("non_existent_file.txt")
        
        with self.assertRaises(FileNotFoundError):
            with open(file_path, 'r') as f:
                f.read()    

if __name__ == "__main__":
    unittest.main()                         