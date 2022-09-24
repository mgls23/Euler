import logging

from euler.util.decorators import timed_function
from individual_solutions.p115 import dp_variable_min


def dynamic_programming_simple(total_blocks):
	starts_1, starts_non_1 = 0, 1
	results = [
		[0, 0],  # 0
		[1, 0],  # 1
		[1, 0],  # 2
	]
	for _ in range(total_blocks - len(results) + 1): results.append([])

	def helper(blocks):
		if not results[blocks]:
			result_minus_1 = helper(blocks - 1)
			results[blocks] = [
				result_minus_1[starts_1] + result_minus_1[starts_non_1],  # starts_1
				1,  # starts_non_1: start with [blocks]
			]

			for block in range(3, blocks + 1):
				result_minus_block = helper(blocks - block)
				results[blocks][starts_non_1] += result_minus_block[starts_1]

		return results[blocks]

	return sum(helper(total_blocks))


def dynamic_programming_solution(total_blocks):
	results = [
		[],  # 0
		[[1]],  # 1
		[[1, 1]],  # 2
	]
	for _ in range(total_blocks - len(results) + 1): results.append([])

	def helper(blocks):
		if not results[blocks] and blocks > 0:
			for result in helper(blocks - 1):
				results[blocks].append([1] + result)

			for first_block in range(3, blocks + 1):
				for result in helper(blocks - first_block):
					if result[0] > 1: continue
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


def q114(number=50):
	return dp_variable_min(number, 3)


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q114)(50) == 16475640049)
