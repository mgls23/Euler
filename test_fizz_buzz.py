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
        pass
        # Floats

if __name__ == '__main__':
    unittest.main()
