from solutions.euler.sequence.continued_fraction import square_root_2_generator
from solutions.euler.util.decorators import timed_function


def numerator_has_more_digits(numerator, denominator):
	return len(str(numerator)) > len(str(denominator))


def q57(number=1000):
	return len([(numerator, denominator) for numerator, denominator in square_root_2_generator(number)
	            if numerator_has_more_digits(numerator, denominator)])


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q57)() == 153)
