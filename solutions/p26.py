import logging
import sys

from solutions.euler.maths.prime import generate_to_sieve
def _string_division_verbose(dividend: int, divisor: int) -> int:
	# INIT -- all words share len() -- satisfying...
	iteration = 0
	dividends = {}
	quotients = []

	logging.info("String Division: %s/%s", dividend, divisor)

	while dividend > 0:
		if dividend in dividends:
			# Print Dividends (version history)
			start = dividends[dividend]
			logging.info(" > ".join(map(str, list(dividends.keys()) + [dividend])))

			# Print quotients (the result)
			quotients_str = list(map(str, quotients))
			quotients_str.insert(start, "(")
			quotients_str.append(")")
			quotients_str.insert(1, ".")
			logging.info("".join(quotients_str))
			return len(dividends) - start

		quotients.append(dividend // divisor)
		dividends[dividend] = iteration

		dividend %= divisor
		dividend *= 10
		iteration += 1

	logging.info(" > ".join(map(str, dividends)))
	logging.info("0." + "".join(map(str, quotients[1:])))
	return 0


def q26():
	""" Q26 :: Reciprocal cycles [https://projecteuler.net/problem=26]

	Find value of d for which 1/d contains the longest recurring cycle
			in its decimal fraction part
	"""

	def string_division(dividend, divisor) -> int:
		iteration = 0
		dividends = {}

		while dividend > 0:
			if dividend in dividends:
				# Recurring cycle found
				return len(dividends) - dividends[dividend]

			dividends[dividend] = iteration
			dividend %= divisor
			dividend *= 10
			iteration += 1

		# No recurring cycle found
		return 0

	return max(generate_to_sieve(1000), key=lambda number: string_division(1, number))


if __name__ == '__main__':
	from solutions.euler.util.decorators import timed_function
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

	for prime in generate_to_sieve(100):
		_string_division_verbose(1, prime)

	assert (timed_function(q26)() == 983)
