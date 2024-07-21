from fractions import Fraction

from solutions.euler.maths.multiplications import gcd as gcd
from solutions.euler.maths.prime import prime_factorize


def slow_phi(number):
	# the number of numbers less than n which are relatively prime to n

	def is_relative_prime(other):
		return gcd(other, number) == 1

	if number < 2: return -1
	return len(list(filter(is_relative_prime, range(2, number)))) \
		+ 1  # 1 is always relatively prime


def calculate_number_of_divisors(n, prime_numbers, n_multiplier=1):
	if n == 1: return 1

	number_of_divisors = 1
	for prime_number in prime_numbers:
		current = 1
		while not n % prime_number:
			current += n_multiplier
			n //= prime_number

			if n == 1:
				number_of_divisors *= current
				# print(original_number, number_of_divisors)
				return number_of_divisors

		number_of_divisors *= current

	raise Exception(n)


def phi(number, primes):
	return _phi(number, *prime_factorize(number, primes).keys())


def _phi(number, *calculated_primes):
	for prime_number in calculated_primes:
		number *= 1 - Fraction(1, prime_number)

	return int(number)
