import logging
from math import prod

from euler.maths.prime import generate_to_sie


def find_pandigital_combinations(numbers: dict):
	combinations = 0
	keys = list(map(set, numbers.keys()))

	def helper(all_keys, used_digits, partition, combined_lengths):
		if combined_lengths == 9:
			nonlocal combinations
			print(all_keys)
			print(list(len(numbers[tuple(sorted(key))]) for key in all_keys))

			combinations += prod(len(numbers[tuple(sorted(key))]) for key in all_keys)
			return

		for i, key in enumerate(keys[partition:], partition):
			if len(key) + combined_lengths > 9:
				return

			if not key.intersection(used_digits):
				helper(all_keys=all_keys + [key], used_digits=used_digits.union(key),
				       partition=i + 1, combined_lengths=combined_lengths + len(key))

	helper([], set(), 0, 0)
	return combinations


def wrong_approach_q118():
	""" There were 2 things wrong with this code
	 - 0 was included (fixed)
	 - assumption was that the biggest pandigital number is 7652413 (as per Q41)
	    => However, this is not true. This is because what Q41 gives me is the largest consecutive pandigital primes
	    => There are definitely 8-digit pandigital prime numbers that can form a set. Therefore, this is wrong
	        and assumed to be impossible approach. (I try to avoid cases where I have to call generate_to_sie > 10 ** 7)
	"""
	pandigital_numbers = {}

	prime_numbers = generate_to_sie(7652413 + 1)
	for prime_number in map(str, prime_numbers):
		unique_digits = set(prime_number)
		if '0' not in unique_digits and len(prime_number) == len(unique_digits):
			footprint = tuple(sorted(unique_digits))
			pandigital_numbers[footprint] = pandigital_numbers.get(footprint, []) + [prime_number]

	return find_pandigital_combinations(pandigital_numbers)


def q118():
	return -1


if __name__ == '__main__':
	import sys
	from euler.util.decorators import timed_function

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	assert (timed_function(q118)() == 30559)
