import unittest
from git_lab import (
    calculate_circle_area,
    celsius_to_fahrenheit,
    is_palindrome,
    calculate_triangle_area,
    is_prime,
    add_numbers
)
import math

class TestUtils(unittest.TestCase):

    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(0), 0)
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)
        self.assertAlmostEqual(calculate_circle_area(2.5), math.pi * (2.5 ** 2))
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))

    def test_calculate_triangle_area(self):
        self.assertEqual(calculate_triangle_area(3, 4), 6.0)
        self.assertEqual(calculate_triangle_area(5, 10), 25.0)
        self.assertEqual(calculate_triangle_area(7.5, 2), 7.5)
        with self.assertRaises(ValueError):
            calculate_triangle_area(-1, 2)
        with self.assertRaises(ValueError):
            calculate_triangle_area(2, -1)

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(30))
        self.assertTrue(is_prime(31))
        self.assertFalse(is_prime(100))

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()