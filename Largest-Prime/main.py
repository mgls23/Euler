from common import prime_generator

def find_primes(x):
	"""
		Finds prime factors* of a given number
		* prime factors :: prime numbers that make up the given number once multiplied together

		Parameters
		----------
			xcopy: int
				the number to conduct the search on primes on

		Returns
		-------
			prime_factors: [int]
				prime numbers that make up the
	"""
	prime_factors = []
	prime_iterator = prime_generator.PrimeGenerator()

	xcopy = x
	while xcopy > 1:
		prime_number = prime_iterator.next()
		if xcopy % prime_number == 0:
			xcopy /= prime_number
			prime_factors.append(prime_number)

		if prime_number > x:
			raise Exception('Lol')

	return prime_factors

if __name__ == '__main__':
	sample = 13195
	desired = 600851475143

	print find_primes(sample)
	print max(find_primes(desired))