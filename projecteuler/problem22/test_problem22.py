import unittest
from problem22 import calc_alpha_val

class TestFuns(unittest.TestCase):
    def test_colin(self):
        self.assertEqual(calc_alpha_val('COLIN'), 53)
    def test_a(self):
        self.assertEqual(calc_alpha_val('A'), 1)
    def test_c(self):
        self.assertEqual(calc_alpha_val('C'), 3)
    def test_n(self):
        self.assertEqual(calc_alpha_val('N'), 14)
    def test_raf(self):
        self.assertEqual(calc_alpha_val('RAF'), (18+1+6) )
    def test_z(self):
        self.assertEqual(calc_alpha_val('Z'), 26 )
