import unittest

import main
from euler.unittests import test_util
from euler.util import maths


class TestMain(unittest.TestCase):
    pass


class TestFizzBuzz(unittest.TestCase):
    pass


def generate_main_tests():
    until_first_3 = {
        0: 0,
        1: 0,
        2: 0,
        3: 3,
    }
    test_util.create_individual_tests(TestMain, until_first_3, function=main.find_sum)

    until_first_5 = {
        4: 3,
        5: 8,
    }
    test_util.create_individual_tests(TestMain, until_first_5, function=main.find_sum)

    until_second_5 = {
        6: 14,
        7: 14,
        8: 14,
        9: 23,
        10: 33,
    }
    test_util.create_individual_tests(TestMain, until_second_5, function=main.find_sum)

    until_15 = {
        11: 33,
        12: 45,
        13: 45,
        14: 45,
        15: 60,
    }
    test_util.create_individual_tests(TestMain, until_15, function=main.find_sum)


def generate_fizz_buzz_tests():
    edge_cases = {
        # Negative Integers
        -1: [],

        # 0s and <3, the smallest
        0: [],
        1: [],
        2: [],

        # Floats

        # String

    }
    test_util.create_batch_test(edge_cases, function=maths.fizz_buzz)

    until_first_5 = {
        3: [3],
        4: [3],
    }
    test_util.create_batch_test(until_first_5, function=maths.fizz_buzz)

    until_second_5 = {
        5: [3, 5],
        6: [3, 5, 6],
        8: [3, 5, 6],
        7: [3, 5, 6],
        9: [3, 5, 6, 9],
    }
    test_util.create_batch_test(until_second_5, function=maths.fizz_buzz)

    until_15 = {
        10: [3, 5, 6, 9, 10],
        11: [3, 5, 6, 9, 10],
        12: [3, 5, 6, 9, 10, 12],
        13: [3, 5, 6, 9, 10, 12],
        14: [3, 5, 6, 9, 10, 12],
        15: [3, 5, 6, 9, 10, 12, 15],
    }
    test_util.create_batch_test(until_15, function=maths.fizz_buzz)


if __name__ == '__main__':
    generate_main_tests()
    unittest.main()
