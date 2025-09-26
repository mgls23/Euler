import logging
import math
import sys

from solutions.euler.util.decorators import timed_function

# If the number is a power of 2, we know how this would be
collatz_sequence = {int(math.pow(2, index - 1)): index for index in range(1, 1000)}


def collatz_length(number):
	def _trailing_zero(x: int) -> int:
		"""count trailing zeros of x>0 via lowbit; faster than loops/while."""
		return (x & -x).bit_length() - 1

	assert number > 0 and number % 2 == 1, "Only odd numbers are considered"

	steps = 0
	stack = []

	while number not in collatz_sequence:
		stack.append((number, steps))

		if number == 1: break

		# Next Collatz Sequence
		number = 3 * number + 1
		steps += 1

		# Make sure no even numbers occur here
		if number % 2 == 0:
			k = _trailing_zero(number)
			number >>= k
			steps += k

	sequence_len = collatz_sequence[number] + steps

	for num, steps in stack:
		collatz_sequence[num] = sequence_len - steps

	return sequence_len


def q14(N=1_000_000):
	""" Q14 :: Longest Collatz sequence [https://projecteuler.net/problem=14]

	Which starting number, under one million, produces the longest chain?
	"""

	return max(range(1, N, 2), key=collatz_length)


if __name__ == '__main__':
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q14)() == 837799)
