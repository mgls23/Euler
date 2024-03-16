import logging

from solutions.euler.maths.palindromes import is_palindrome
from solutions.euler.maths.prime import generate_to_sie, is_prime_robin_miller
from solutions.euler.util.decorators import timed_function


def see_pattern():
	prime_numbers = generate_to_sie(10 ** 6)

	squared = set()
	reversible_prime_squares = []

	for prime_number in prime_numbers:
		square_prime = str(prime_number ** 2)
		if not is_palindrome(square_prime):
			squared.add(square_prime)
			if square_prime[::-1] in squared:
				reversible_prime_squares.extend((square_prime[::-1], square_prime))

	# print(len(reversible_prime_squares))
	# print([int(int(prime) ** 0.5) for prime in reversible_prime_squares])
	return reversible_prime_squares


def q808():
	# REVISIT :: I don't understand why this works I just noticed the pattern from above and applied
	squared = set()

	reversible_squared_primes = []
	digits = [3, 1]
	while len(reversible_squared_primes) < 50:
		if is_prime_robin_miller(number := int(''.join(map(str, digits[::-1])))) \
				and not is_palindrome(squared_prime := str(number ** 2)):
			squared.add(squared_prime)
			if squared_prime[::-1] in squared:
				reversible_squared_primes.extend((squared_prime, squared_prime[::-1]))

		digits[0] += 1
		j = 0
		while digits[j] > 3:
			digits[j] = 0
			j += 1
			if j == len(digits): digits.append(0)
			digits[j] += 1

	return sum(map(int, reversible_squared_primes[:50]))


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q808)() == 3807504276997394)
