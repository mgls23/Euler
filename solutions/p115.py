import logging

from euler.strings.number_to_string import MILLION
from euler.util.decorators import timed_function


def dp_variable_min(total_blocks, minimum_block_size):
	""" This is just p114 but with variable minimum_block size
	Minor adjustments have been made
	"""
	starts_1, starts_non_1 = 0, 1
	results = [[0, 0]]

	# Adjustment 1 ::
	for _ in range(minimum_block_size - 1):
		results.append([1, 0])

	for _ in range(total_blocks - len(results) + 1):
		results.append([])

	def helper(blocks):
		if not results[blocks]:
			result_minus_1 = helper(blocks - 1)
			results[blocks] = [
				result_minus_1[starts_1] + result_minus_1[starts_non_1],  # starts_1
				1,  # starts_non_1: start with [blocks]
			]

			# Adjustment 2 ::
			for block in range(minimum_block_size, blocks + 1):
				result_minus_block = helper(blocks - block)
				results[blocks][starts_non_1] += result_minus_block[starts_1]

		return results[blocks]

	return sum(helper(total_blocks))


def q115(m=50):
	# Just a large upper bound large
	for n in range(3, 100000):
		if dp_variable_min(total_blocks=n, minimum_block_size=m) > MILLION:
			return n


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q115)(10) == 57)
	assert (timed_function(q115)(50) == 168)
