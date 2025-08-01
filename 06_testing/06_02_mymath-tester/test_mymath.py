# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.
import unittest
import mymath

class Test_mymath(unittest.TestCase):
    def test_subtract_divide(self):
        # Test for correct results
        result = mymath.subtract_divide(10, 5, 3)
        self.assertEqual(result, 5.0)   

    def test_subtract_divide_zero_division(self):
        # Test for CustomZeroDivisionError
        with self.assertRaises(mymath.CustomZeroDivsionError):
            mymath.subtract_divide(10, 5, 5)

if __name__ == "__main__":
    unittest.main()

