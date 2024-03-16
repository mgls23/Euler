from solutions.euler.maths.prime import generate_to_sie
from solutions.euler.util.decorators import timed_function


def number_of_distinct_primes(up_to):
	""" Use reversed version of sieve to generate this """
	distinct_primes = [0] * up_to
	for prime in generate_to_sie(up_to):
		distinct_primes[prime::prime] = [distinct_prime + 1 for distinct_prime in distinct_primes[prime::prime]]

	return distinct_primes


def q47(consecutive=4):
	upper_range = 150000

	distinct_prime_factors = number_of_distinct_primes(upper_range)
	for start_index, length in enumerate(distinct_prime_factors):
		for index in range(start_index, start_index + consecutive):
			if distinct_prime_factors[index] != consecutive: break

		else:
			return start_index


if __name__ == '__main__':
	assert (timed_function(q47)() == 134043)
