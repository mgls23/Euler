import unittest

from solutions.euler.something import ways_to_express_number, ways_to_express, _f_


class TestSomething(unittest.TestCase):
    def test_fn(self):
        answers = {
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 7,
        }

        for args, answer in answers.items():
            self.assertEqual(ways_to_express_number(args), answer)

    def test_fn_(self):
        answers = {
            (6, 4): 9,
            # 2: 2,
            # 3: 3,
            # 4: 5,
            # 5: 7,
        }

        for args, answer in answers.items():
            self.assertEqual(ways_to_express(*args), answer)

    def test_fn__(self):
        answers = {
            (6, 2): 4,
            (4, 2): 3,
        }

        for args, answer in answers.items():
            self.assertEqual(_f_(*args), answer)

    def test_something(self):
        for i in [20, 50, 100]:
            self.assertEqual(ways_to_express_number(i), ways_to_express(i, i - 1) + 1, i)
