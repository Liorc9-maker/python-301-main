# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.
import unittest
import math

class TestMathModule(unittest.TestCase):
    def test_sqrt(self):
        # Test the square root function
        self.assertEqual(math.sqrt(4), 2)
        self.assertEqual(math.sqrt(9), 3)
        self.assertRaises(ValueError, math.sqrt, -1)

    def test_factorial(self):
        # Test the factorial function
        self.assertEqual(math.factorial(0), 1)
        self.assertEqual(math.factorial(5), 120)
        self.assertRaises(ValueError, math.factorial, -1)


if __name__ == "__main__":
    unittest.main()        
