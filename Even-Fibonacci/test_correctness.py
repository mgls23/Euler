import unittest
import main


class TestFibonacciIterator(unittest.TestCase):
	pass


def create_individual_test(x, expected):
	def case(self):
		self.assertEquals(x, expected)

	return case


def create_fibonacci_tests():
	correct_sequence = [1, 2, 3, 5, 8, 13, 21, 34, 55, ]
	iterator = main.FibonacciIterator()

	for index in range(len(correct_sequence)):
		correct_value = correct_sequence[index]
		test_value = iterator.get_nth_fibonacci(index + 1)

		test_case = create_individual_test(correct_value, test_value)
		test_name = 'test_fibonacci_{}'.format(index)
		setattr(TestFibonacciIterator, test_name, test_case)


if __name__ == '__main__':
	create_fibonacci_tests()
	unittest.main()
