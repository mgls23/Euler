import unittest


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        is_palindrome_check = {
            1: True,
            10: False,
            11: True,
            121: True,
            1231: False,
        }

        from solutions.euler.maths.palindromes import _is_palindrome
        for number, is_palindrome_ in is_palindrome_check.items():
            self.assertEqual(is_palindrome_, _is_palindrome(number))
