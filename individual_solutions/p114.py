import logging

from euler.util.decorators import timed_function


def dynamic_programming_solution(total_blocks):
	results = [
		[],  # 0
		[[1]],  # 1
		[[1, 1]],  # 2
	]
	for _ in range(total_blocks - len(results) + 1): results.append([])

	def helper(blocks):
		if not results[blocks] and blocks > 0:
			for first_block in [1] + list(range(3, blocks + 1)):
				for result in helper(blocks - first_block):
					if first_block > 1 and result[0] > 1: continue
					results[blocks].append([first_block] + result)

			results[blocks].append([blocks])

		return results[blocks]

	helper(total_blocks)
	return results[total_blocks]


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
	return len(brute_force(30))


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q114)() == 38182)
