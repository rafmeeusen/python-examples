import unittest
from problem21 import proper_divisors

class TestFuns(unittest.TestCase):
    def test1(self):
        self.assertEqual(proper_divisors(1), [1])
    def test2(self):
        self.assertEqual(proper_divisors(2), [1])
    def test3(self):
        self.assertEqual(proper_divisors(3), [1])
    def test4(self):
        self.assertEqual(proper_divisors(4), [1, 2])
    def test5(self):
        self.assertEqual(proper_divisors(5), [1])
    def test6(self):
        self.assertEqual(proper_divisors(6), [1, 2, 3])
    def test7_to_10(self):
        self.assertEqual(proper_divisors(7), [1])
        self.assertEqual(proper_divisors(8), [1, 2, 4])
        self.assertEqual(proper_divisors(9), [1, 3])
        self.assertEqual(proper_divisors(10), [1, 2, 5])
    def test_known_large(self):
        self.assertEqual(proper_divisors(220), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55 ,110])
        self.assertEqual(proper_divisors(284), [1, 2, 4, 71 ,142])


