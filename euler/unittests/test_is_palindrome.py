import unittest

from euler.largest_palindrome_product import is_palindrome


class TestFibonacciIterator(unittest.TestCase):
    def test_is_palindrome(self):
        is_palindrome_check = {
            1: True,
            10: False,
            11: True,
            121: True,
            1231: False,
        }

        for number, is_palindrome_ in is_palindrome_check.items():
            self.assertEqual(is_palindrome_, is_palindrome(number))
