import logging

from euler.util.decorators import timed_function


def brute_force(total_blocks):
	solutions = []

	def helper(remaining, path):
		if remaining <= 2:
			assert remaining >= 0
			solutions.append(path + [1] * remaining)
			return

		block_lengths = [1]
		if not path or path[-1] == 1: block_lengths += list(range(3, remaining + 1))
		for block_length in block_lengths:
			helper(remaining - block_length, path + [block_length])

	helper(total_blocks, [])
	return solutions


def q114():
	result = brute_force(50)
	# this does not work and neither do I expect it to
	print(result)
	return len(result)


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q114)() == 38182)
