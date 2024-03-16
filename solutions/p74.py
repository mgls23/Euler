from math import factorial

from solutions.euler.util.decorators import timed_function


def brute_force():
	def repeating_terms(number):
		pattern = []
		while number not in pattern:
			pattern.append(number)
			every_digit = map(int, str(number))
			number = sum(map(factorial, every_digit))

		return pattern

	count = 0
	for number in range(10 ** 6):
		pattern = repeating_terms(number)
		if len(pattern) == 60:
			logging.debug(f'Number={number}, Pattern={pattern[1:]}')
			count += 1

	return count


def remember_chain_lengths():
	def repeating_pattern(number, previous_lengths):
		pattern = []
		while number not in pattern:
			pattern.append(number)
			every_digit = map(int, str(number))
			number = sum(map(factorial, every_digit))

			if number in previous_lengths:
				return len(pattern) + previous_lengths[number]

		return len(pattern)

	previous_lengths = {}
	count = 0
	for number in range(10 ** 6):
		sequence_length = repeating_pattern(number, previous_lengths)
		previous_lengths[number] = sequence_length

		if sequence_length == 60: count += 1

	return count


def not_sure():
	# @mathgod's solution [https://projecteuler.net/thread=74]
	# Observe that in the brute_force - the first item in the chain always seemed to be 367945.
	# Combination of 0/1,4,7,9 OR 2,2,3,4,7,9
	permutation_of_1479 = factorial(4)
	permutation_of_0479 = factorial(3) * 3
	permutation_of_223479 = factorial(6) // 2
	return permutation_of_1479 + permutation_of_0479 + permutation_of_223479


def p74():
	return remember_chain_lengths()


if __name__ == '__main__':
	import logging
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(p74)() == 402)
