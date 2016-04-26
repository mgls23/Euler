import argparse

from smallest_multiple import smallest_multiple
from common import prime
from const import problemArgs


# Q3 :: Largest Prime Factor
def find_primes(x=600851475143):
	"""
		Finds prime factors* of a given number
		* prime factors :: prime numbers that make up the given number once multiplied together

		Parameters
		----------
			x: int
				the number to conduct the search on primes on

		Returns
		-------
			prime_factors: [int]
				prime numbers that make up the
	"""
	prime_factors, prime_iterator, prime_number, x_copy = [], prime.PrimeGenerator(), 1, x

	while x_copy > 1 and prime_number < x:
		prime_number = prime_iterator.next()
		if x_copy % prime_number == 0:
			x_copy /= prime_number
			prime_factors.append(prime_number)

	return max(prime_factors)


# Q6 :: Sum Square Difference
def square_difference(n=100):
	"""
	(1 + 2 + 3 + ... n)^2
	 = ((n * (n + 1)) / 2) ^ 2

	1^2 + 2^2 + 3^2 + ... n^2
     [BRUTE FORCE]

	Args
	----
		n: int

	Returns
	-------

	"""
	square_of_sum = ((n + 1) * n / 2) ** 2
	sum_of_square = sum([i ** 2 for i in range(n + 1)])
	return square_of_sum - sum_of_square


# Q7 :: 10001st prime
def q_10001th_prime(n=10001):
	return prime.PrimeGenerator().generate_nth(n)


# Q8 :: Adjacent Multiplicand
def adjacent(x, window_size=13):
	"""

	Parameters
	----------
	x
	window_size

	Returns
	-------

	"""
	assert x and window_size, "Please provide a number that we could run some cool maths on"

	# Break down x into a list
	x = [int(strx) for strx in (type(x) == int) and str(x) or x]
	y = x[:-1]
	# z = len(x) - window_size
	for iteration_count in range(1, window_size):
		for index in range(len(y) - 1):
			y[index] *= x[index + iteration_count]

		y.pop(-1)

	# if iteration_count == z:
	# 	break

	return max(y)


problemHandler = \
	{
		# 1: fizz_buzz,

		5: smallest_multiple,
		6: square_difference,
		7: q_10001th_prime,
		8: adjacent,
	}

if __name__ == '__main__':
	# Configure Parser + Parse
	parser = argparse.ArgumentParser(description='Project Euler, dyxogus implementation')
	parser.add_argument('n', metavar='n', type=int, help='The Problem that needs to be solved')
	args = parser.parse_args()

	# Execute Problem
	result = problemHandler[args.n](**problemArgs[args.n])
	print result
