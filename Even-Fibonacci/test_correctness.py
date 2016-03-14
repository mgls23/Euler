import unittest
import main


class TestFibonacciIterator(unittest.TestCase):
	pass


def create_individual_test(x, expected):
	def case(self):
		self.assertEquals(x, expected)

	return case


def create_batch_tests():
	def case(self):
		pass

	return case


def create_fibonacci_tests():
	fibonacci_sequence = [1, 2, 3, 5, 8, 13, 21, 34, 55, ]
	iterator = main.FibonacciIterator()
	for index, value in enumerate(fibonacci_sequence):
		test_case = create_individual_test(iterator.next(), value)
		test_name = 'test_fibonacci_{}'.format(index)
		setattr(TestFibonacciIterator, test_name, test_case)

if __name__ == '__main__':
	create_fibonacci_tests()
	unittest.main()
