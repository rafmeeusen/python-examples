import unittest
from rafsint import RafsInt

class TestRafsInt (unittest.TestCase):

    def test_even_odd(self):
        testint = RafsInt(0)
        self.assertTrue(RafsInt(0).is_even())
        self.assertTrue(RafsInt(1).is_odd())
        self.assertTrue(RafsInt(2).is_even())
        self.assertTrue(RafsInt(3).is_odd())
        self.assertTrue(RafsInt(4).is_even())
        self.assertFalse(RafsInt(0).is_odd())
        self.assertFalse(RafsInt(1).is_even())
        self.assertFalse(RafsInt(2).is_odd())
        self.assertFalse(RafsInt(3).is_even())
        self.assertFalse(RafsInt(4).is_odd())

    def test_prime(self):
        self.assertFalse(RafsInt(0).is_prime())
        self.assertFalse(RafsInt(1).is_prime())
        self.assertTrue(RafsInt(2).is_prime())
        self.assertTrue(RafsInt(3).is_prime())
        self.assertFalse(RafsInt(4).is_prime())
        self.assertTrue(RafsInt(5).is_prime())
        self.assertFalse(RafsInt(6).is_prime())
        self.assertTrue(RafsInt(7).is_prime())
        self.assertFalse(RafsInt(8).is_prime())

    def test_perfect(self):
        self.assertFalse(RafsInt(0).is_perfect())
        self.assertFalse(RafsInt(1).is_perfect())
        self.assertFalse(RafsInt(2).is_perfect())
        self.assertFalse(RafsInt(3).is_perfect())
        self.assertFalse(RafsInt(4).is_perfect())
        self.assertFalse(RafsInt(5).is_perfect())
        self.assertTrue(RafsInt(6).is_perfect())

    def test_get_prime_factorization(self):
        self.assertEqual(RafsInt(2).get_prime_factorization_dict(), {2:1})
        self.assertEqual(RafsInt(3).get_prime_factorization_dict(), {2:0,3:1})
        self.assertEqual(RafsInt(4).get_prime_factorization_dict(), {2:2})
        self.assertEqual(RafsInt(6).get_prime_factorization_dict(), {2:1,3:1})
        self.assertEqual(RafsInt(12).get_prime_factorization_dict(), {2:2,3:1})

    def test_get_nr_of_divisors(self):
        self.assertEqual(RafsInt(1).get_nr_of_divisors(), 1)
        self.assertEqual(RafsInt(2).get_nr_of_divisors(), 2)
        self.assertEqual(RafsInt(3).get_nr_of_divisors(), 2)
        self.assertEqual(RafsInt(4).get_nr_of_divisors(), 3)
        self.assertEqual(RafsInt(5).get_nr_of_divisors(), 2)
        self.assertEqual(RafsInt(6).get_nr_of_divisors(), 4)
        self.assertEqual(RafsInt(7).get_nr_of_divisors(), 2)
        self.assertEqual(RafsInt(8).get_nr_of_divisors(), 4)
        self.assertEqual(RafsInt(19).get_nr_of_divisors(), 2)
        self.assertEqual(RafsInt(20).get_nr_of_divisors(), 6)
        self.assertEqual(RafsInt(24).get_nr_of_divisors(), 8)

    def test_is_triangular(self):
        self.assertTrue(RafsInt(0).is_triangular())
        self.assertTrue(RafsInt(1).is_triangular())
        self.assertFalse(RafsInt(2).is_triangular())
        self.assertTrue(RafsInt(3).is_triangular())
        self.assertFalse(RafsInt(4).is_triangular())
        self.assertFalse(RafsInt(5).is_triangular())
        self.assertTrue(RafsInt(6).is_triangular())
        self.assertFalse(RafsInt(7).is_triangular())
        self.assertFalse(RafsInt(8).is_triangular())
        self.assertFalse(RafsInt(9).is_triangular())
        self.assertTrue(RafsInt(10).is_triangular())
        self.assertTrue(RafsInt(15).is_triangular())
        self.assertTrue(RafsInt(21).is_triangular())
        self.assertTrue(RafsInt(28).is_triangular())
        self.assertTrue(RafsInt(36).is_triangular())
        self.assertTrue(RafsInt(45).is_triangular())
        self.assertTrue(RafsInt(55).is_triangular())
        self.assertTrue(RafsInt(66).is_triangular())


if __name__ == '__main__':
    unittest.main()


