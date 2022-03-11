from euler.maths.prime import generate_to_sie
from euler.util.decorators import timed_function


def coin_partition_leaner(number):
	prime_numbers = list(reversed(generate_to_sie(number + 1)))

	count = 0

	def helper(start_offset, remaining):
		if remaining == 0:
			nonlocal count
			count += 1

		if remaining <= 0:
			return

		for offset, prime_number in enumerate(prime_numbers[start_offset:], start_offset):
			helper(offset, remaining - prime_number)

	helper(start_offset=0, remaining=number)
	return count


def coin_partition(number):
	prime_numbers = list(reversed(generate_to_sie(number + 1)))
	logging.debug(f'Input = {number}, Prime Numbers = {prime_numbers}')

	results = []

	def helper(start_offset, chosen, remaining):
		if remaining == 0: results.append(chosen[:])
		if remaining <= 0: return

		for offset, prime_number in enumerate(prime_numbers[start_offset:], start_offset):
			chosen.append(prime_number)
			helper(offset, chosen, remaining - prime_number)
			chosen.pop()

	helper(start_offset=0, chosen=[], remaining=number)
	logging.debug(results)
	return len(results)


def q77(more_than=5000):
	for number in range(2, 10000):
		result = coin_partition_leaner(number)
		if result > more_than:
			return number

	return -1


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q77)() == 71)
