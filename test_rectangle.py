import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 2)
       self.assertEqual(res, 20)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_perimeter_1_mul(self):
       res = perimeter(5, 4)
       self.assertEqual(res, 18)