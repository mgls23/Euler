import unittest

import maths
import main


class TestMain(unittest.TestCase):
	pass


class TestFizzBuzz(unittest.TestCase):
	pass


def create_batch_test(cases, function):
	def case(self):
		for key, value in cases:
			self.assertEqual(function(key), value)

	return case


def create_individual_test(function, provided, expected):
	def case(self):
		self.assertEqual(function(provided), expected)

	return case


def create_individual_tests(test_unit, cases, function):
	for key, value in cases.iteritems():
		test_name = 'test_{}'.format(key)
		test = create_individual_test(function=function, provided=key, expected=value)
		setattr(test_unit, test_name, test)


def generate_main_tests():
	until_first_3 = {
		0: 0,
		1: 0,
		2: 0,
		3: 3,
	}
	create_individual_tests(TestMain, until_first_3, function=main.find_sum)

	until_first_5 = {
		4: 3,
		5: 8,
	}
	create_individual_tests(TestMain, until_first_5, function=main.find_sum)

	until_second_5 = {
		6: 14,
		7: 14,
		8: 14,
		9: 23,
		10: 33,
	}
	create_individual_tests(TestMain, until_second_5, function=main.find_sum)

	until_15 = {
		11: 33,
		12: 45,
		13: 45,
		14: 45,
		15: 60,
	}
	create_individual_tests(TestMain, until_15, function=main.find_sum)


if __name__ == '__main__':
	generate_main_tests()
	unittest.main()


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
	create_batch_test(edge_cases, function=maths.fizz_buzz)

	until_first_5 = {
		3: [3],
		4: [3],
	}
	create_batch_test(until_first_5, function=maths.fizz_buzz)

	until_second_5 = {
		5: [3, 5],
		6: [3, 5, 6],
		8: [3, 5, 6],
		7: [3, 5, 6],
		9: [3, 5, 6, 9],
	}
	create_batch_test(until_second_5, function=maths.fizz_buzz)

	until_15 = {
		10: [3, 5, 6, 9, 10],
		11: [3, 5, 6, 9, 10],
		12: [3, 5, 6, 9, 10, 12],
		13: [3, 5, 6, 9, 10, 12],
		14: [3, 5, 6, 9, 10, 12],
		15: [3, 5, 6, 9, 10, 12, 15],
	}
	create_batch_test(until_15, function=maths.fizz_buzz)
