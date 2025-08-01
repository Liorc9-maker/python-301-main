# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.
import unittest
import classy_shapes
from math import pi


class TestShapes(unittest.TestCase):
    def setUp(self):
        self.circle = classy_shapes.Circle(3)
        self.rectangle = classy_shapes.Rectangle(7, 3)

    def test_circle_area(self):
        self.assertAlmostEqual(self.circle.area(), pi * 3 ** 2)

    def test_circle_circumference(self):
        self.assertAlmostEqual(self.circle.circumference(), pi * 3 * 2)

    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 7 * 3)

    def test_rectangle_perimeter(self):
        self.assertEqual(self.rectangle.perimeter(), 2 * (7 + 3))
if __name__ == '__main__':
    unittest.main()
