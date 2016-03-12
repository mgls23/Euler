import unittest

import fizz_buzz
import main


def check_fizz_buzz(self, input, output):
    self.assertEqual(fizz_buzz.fizz_buzz(input), output)


class TestFizzBuzz(unittest.TestCase):
    def test_edge_cases(self):
        # Zero Cases
        check_fizz_buzz(self, 0, [])
        check_fizz_buzz(self, 1, [])
        check_fizz_buzz(self, 2, [])

        # Negative Integers
        check_fizz_buzz(self, -1, [])

    def test_incompatible_types(self):
        # Floats
        pass

        # Strings
        pass

    def test_basic_cases(self):
        check_fizz_buzz(self, 3, [3])
        check_fizz_buzz(self, 4, [3])
        check_fizz_buzz(self, 5, [3, 5])
        check_fizz_buzz(self, 6, [3, 5, 6])
        check_fizz_buzz(self, 8, [3, 5, 6])
        check_fizz_buzz(self, 7, [3, 5, 6])
        check_fizz_buzz(self, 9, [3, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
