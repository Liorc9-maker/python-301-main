# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)
import unittest
import math

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Returns the product of two numbers."""
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        """Test the add_numbers function."""
        self.assertEqual(add_numbers(2, 3), 5)  # Test with positive integers
        self.assertEqual(add_numbers(-1, 1), 0)  # Test with negative and positive integers

    def test_multiply_numbers(self):
        """Test the multiply_numbers function."""
        self.assertEqual(multiply_numbers(2, 3), 6)  # Test with positive integers
        self.assertEqual(multiply_numbers(-1, 1), -1)  # Test with negative and positive integers

    def test_add_numbers_fail(self):
        """Test that fails intentionally."""
        self.assertEqual(add_numbers(2, 2), 5)  # This will fail


if __name__ == "__main__":
    unittest.main()        