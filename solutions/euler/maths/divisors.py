import logging
import math

from solutions.euler.maths.prime import is_prime, prime_factorize


def sum_of_divisors(n, primes):
	return math.prod(
		[_sum_of_divisors(prime_number, power)
		 for prime_number, power in prime_factorize(n, primes).items()]
	)


def _sum_of_divisors(prime_number, power):
	return (prime_number ** (power + 1) - 1) // (prime_number - 1)


def sum_of_proper_divisors(n, primes):
	return sum_of_divisors(n, primes) - n


def factorise_by(number, prime_number):
	""" Returns 1 iteration of decompose to prime powers - where it shows how many times
	the prime number factors into this number

	:param number: int
	:param prime_number: int
	:return: remaining_number, power
	"""
	power = 0
	while number % prime_number == 0:
		number //= prime_number
		power += 1

	return number, power


# functions introduced by 21, 23
def is_perfect_number(number):
	# Perfect number has 2 interesting properties:
	# 1. perfect_number => 2^n * y   # where y is a prime
	# 2. 2^(n+1) = y+1
	# Apparently - this is Euclid-Euler theorem
	#   [https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem]
	y, n = factorise_by(number, 2)
	return pow(2, n + 1) == (y + 1) and is_prime(y)


def generate_perfect_numbers(upper_limit=None):
	def power_to_perfect_number(power):
		return pow(2, 2 * power + 1) - pow(2, power)

	i = 0
	while upper_limit is None or power_to_perfect_number(i) < upper_limit:
		i += 1
		if is_prime(pow(2, i + 1) - 1):
			yield power_to_perfect_number(i)


def is_abundant_number(number, primes):
	return sum_of_proper_divisors(number, primes) > number


def generate_abundant_number(n, prime_powers):
	# hmm not sure about this one
	lhs = pow(2, n + 1)
	rhs = 1
	for p, m in prime_powers.items():
		numerator, denominator = multiply_out(p, m)

		rhs *= numerator
		lhs *= denominator

	logging.debug(f'{lhs, rhs}')

	if lhs > rhs:
		abundant_number = pow(2, n)
		for p, m in prime_powers.items():
			abundant_number *= pow(p, m)
		return abundant_number

	return -1


def multiply_out(prime_number, power):
	numerator = pow(prime_number, power + 1) - 1
	denominator = pow(prime_number, power) - 1

	logging.debug(f'{prime_number, power, numerator, denominator}')

	return numerator, denominator
