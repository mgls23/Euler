from functools import lru_cache

from euler.strings.number_to_string import MILLION
from euler.util.decorators import timed_function


def coin_partition(number):
	@lru_cache(maxsize=None)
	def helper(remaining, no_higher_than):
		if no_higher_than == 1: return 1
		if remaining <= 2: return max(remaining, 1)

		return sum(helper(remaining - partition, partition)
		           for partition in range(no_higher_than, 0, -1))

	return helper(number, number)


def q78(divisible_by=10):
	for i in range(2, 100000):
		result = coin_partition(i)
		print(i, result)
		# if result % divisible_by == 0:
		# 	print(i, result)
			# return result


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(coin_partition)(5) == 7)
	assert (timed_function(q78)() == -1)
