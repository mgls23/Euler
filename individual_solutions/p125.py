import logging


def squared(number: int):
	return number * number


def brute_force(upper_bound=10):
	square_numbers = list(map(squared, range(1, upper_bound + 1)))
	sums_of_squares = []


def q125():
	return -1


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q125)() == -1)
