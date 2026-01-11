"""
Problem 7: 10001st prime
https://projecteuler.net/problem=7

Find the 10001st prime number.

Uses a sieve up to an upper bound estimated by the prime number theorem.
"""
import math

from solutions.euler.maths.prime import generate_to_sieve


def _nth_prime_upper_bound(n: int) -> int:
	"""Upper bound for nth prime (n >= 6)."""
	return int(n * (math.log(n) + math.log(math.log(n)))) + 3


def q7(n: int = 10001) -> int:
	"""Return the nth prime."""
	if n < 1:
		raise ValueError("n must be >= 1")

	if n <= 5:
		return [2, 3, 5, 7, 11][n - 1]

	limit = _nth_prime_upper_bound(n)
	while True:
		primes = generate_to_sieve(limit)
		if len(primes) >= n:
			return primes[n - 1]

		limit *= 2


if __name__ == '__main__':
	from solutions.euler.util.runner import run_solution

	run_solution(q7, 7)
