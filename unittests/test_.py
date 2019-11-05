import unittest

from euler.something import f, _f, _f_


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
            self.assertEqual(f(args), answer)

    def test_fn_(self):
        answers = {
            (6, 4): 9,
            # 2: 2,
            # 3: 3,
            # 4: 5,
            # 5: 7,
        }

        for args, answer in answers.items():
            self.assertEqual(_f(*args), answer)

    def test_fn__(self):
        answers = {
            (6, 2): 4,
            (4, 2): 3,
        }

        for args, answer in answers.items():
            self.assertEqual(_f_(*args), answer)

    def test_something(self):
        for i in [20, 50, 100]:
            self.assertEqual(f(i), _f(i, i - 1) + 1, i)
