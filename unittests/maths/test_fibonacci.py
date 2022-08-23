from euler.maths.fibonacci import FibonacciIterator, NFibonacciIterator
from euler.strings.number_to_string import MILLION


def test_fibonacci_sequence():
	_test_fibonacci_sequence_with_one_1()
	_test_fibonacci_sequence_with_two_1s()


def _test_fibonacci_sequence_with_one_1():
	iterator = FibonacciIterator(start_with_two_1s=False)
	assert iterator.sequence == [1, 2]

	assert iterator.calculate_nth(10) == 89
	assert iterator.sequence == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

	iterator.set_upper_bound(50)
	assert iterator.sequence == [1, 2, 3, 5, 8, 13, 21, 34]

	iterator.set_upper_bound(100)
	assert iterator.sequence == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def _test_fibonacci_sequence_with_two_1s():
	iterator = FibonacciIterator(start_with_two_1s=True)
	assert iterator.sequence == [1, 1]

	assert iterator.calculate_nth(10) == 55
	assert iterator.sequence == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

	iterator.set_upper_bound(50)
	assert iterator.sequence == [1, 1, 2, 3, 5, 8, 13, 21, 34]

	iterator.set_upper_bound(100)
	assert iterator.sequence == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_n3_fibonacci_sequence():
	iterator = FibonacciIterator()

	n3_iterator = NFibonacciIterator.n3()
	assert n3_iterator.sequence == [2, 8]

	n3_iterator.set_upper_bound(4 * MILLION)
	iterator.set_upper_bound(4 * MILLION)
	assert n3_iterator.sequence == list(filter(lambda number: number % 2 == 0, iterator.sequence))
