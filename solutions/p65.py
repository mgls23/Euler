import itertools

from solutions.euler.util.decorators import timed_function


def q65(n=100):
	number = 2
	periods = list(itertools.chain(*[[1, 2]] + [[1, 1, 2 * i] for i in range(2, (n // 3) + 2)]))[1:n - 1]

	denominator_2, numerator_2 = 1, number
	denominator_1, numerator_1 = 1, 3

	for period in periods:
		denominator = denominator_1 * period + denominator_2
		numerator = numerator_1 * period + numerator_2

		denominator_2, numerator_2 = denominator_1, numerator_1
		denominator_1, numerator_1 = denominator, numerator

	return sum(map(int, str(numerator)))


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q65)(10) == 17)
	assert (timed_function(q65)() == 272)
	# timed_function(q65_reference)()
