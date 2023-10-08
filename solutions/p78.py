from .euler.strings.number_to_string import MILLION
from .euler.util.decorators import timed_function


def coin_partition(number):
	# TODO :: construct 2D matrix and use DP

	def helper(remaining, no_higher_than):
		if no_higher_than == 1: return 1
		if remaining <= 2: return max(remaining, 1)

		return sum(helper(remaining - partition, partition)
		           for partition in range(no_higher_than, 0, -1))

	return helper(number, number)


def q78(number=MILLION):
	# for i in range(2, 100000):
	# 	result = coin_partition(i)
	# 	if result % number == 0:
	# 		return result

	for i in range(100):
		print(f'{i} = {coin_partition(i)}')


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(coin_partition)(5) == 7)
	assert (timed_function(q78)() == -1)
