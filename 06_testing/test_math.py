import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
        # snip
    
    def test_ceil_rounds_up(self):
        self.assertEqual(math.ceil(3.4), 4)
        # snip
    def test_sqrt_positive(self):
        self.assertEqual(math.sqrt(16), 4)

        # snip



if __name__ == "__main__":
    unittest.main()
