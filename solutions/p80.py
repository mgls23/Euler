import math
from decimal import Decimal, getcontext

from solutions.euler.util.decorators import timed_function


def square_root_n(number, iteration_count=100000):
	"""
		- newton's method - not sure about the intricate details (like precision, and exit-condition)
		- more research is needed
	"""
	getcontext().prec = 110

	x_n = Decimal(int(math.sqrt(number)))  # we can do this "manually" but not worth effort

	f_x = lambda x: x ** 2 - number
	df_x = lambda x: number * x

	for iteration in range(iteration_count):
		if (x_n_1 := x_n - (f_x(x_n) / df_x(x_n))) == x_n:
			return x_n

		x_n = x_n_1

	raise Exception(f'Did not reach the solution: {number}')


def digit_sum_of_100(number):
	square_root = square_root_n(number)
	first_100_digits = str(square_root).replace('.', '')[:100]
	return sum(map(int, first_100_digits))


def q80():
	irrational_numbers = filter(lambda n: math.sqrt(n) % 1 != 0, range(2, 100 + 1))
	return sum(map(digit_sum_of_100, irrational_numbers))


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(digit_sum_of_100)(2) == 475)
	assert (timed_function(q80)() == 40886)
