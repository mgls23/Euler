import unittest

import maths
import main


class TestMain(unittest.TestCase):
	def execute_main(self, x, expected):
		self.assertEqual(main.find_sum(x), expected)

	def test_until_first_3(self):
		self.execute_main(0, 0)
		self.execute_main(1, 0)
		self.execute_main(2, 0)
		self.execute_main(3, 3)

	def test_until_first_5(self):
		self.execute_main(4, 3)
		self.execute_main(5, 8)

	def test_until_second_5(self):
		self.execute_main(6, 14)
		self.execute_main(7, 14)
		self.execute_main(8, 14)
		self.execute_main(9, 23)
		self.execute_main(10, 33)

	def test_until_third_5(self):
		self.execute_main(11, 33)
		self.execute_main(12, 45)
		self.execute_main(13, 45)
		self.execute_main(14, 45)
		self.execute_main(15, 60)

	def test_extreme_numbers(self):
		self.execute_main(1000, )

	def test_edge_cases(self):
		pass


class TestFizzBuzz(unittest.TestCase):
	def execute_fizz_buzz(self, x, expected):
		self.assertEqual(maths.fizz_buzz(x), expected)

	def test_edge_cases(self):
		# Zero Cases
		self.execute_fizz_buzz(0, [])
		self.execute_fizz_buzz(1, [])
		self.execute_fizz_buzz(2, [])

		# Negative Integers
		self.execute_fizz_buzz(-1, [])

	def test_incompatible_types(self):
		# Floats
		pass

		# Strings
		pass

	def test_until_first_5(self):
		self.execute_fizz_buzz(3, [3])
		self.execute_fizz_buzz(4, [3])

	def test_until_second_5(self):
		self.execute_fizz_buzz(5, [3, 5])
		self.execute_fizz_buzz(6, [3, 5, 6])
		self.execute_fizz_buzz(8, [3, 5, 6])
		self.execute_fizz_buzz(7, [3, 5, 6])
		self.execute_fizz_buzz(9, [3, 5, 6, 9])

	def test_until_15(self):
		self.execute_fizz_buzz(10, [3, 5, 6, 9, 10])
		self.execute_fizz_buzz(11, [3, 5, 6, 9, 10])
		self.execute_fizz_buzz(12, [3, 5, 6, 9, 10, 12])
		self.execute_fizz_buzz(13, [3, 5, 6, 9, 10, 12])
		self.execute_fizz_buzz(14, [3, 5, 6, 9, 10, 12])
		self.execute_fizz_buzz(15, [3, 5, 6, 9, 10, 12, 15])


if __name__ == '__main__':
	unittest.main()
