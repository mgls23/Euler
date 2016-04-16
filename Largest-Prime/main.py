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
	prime_iterator = PrimeGenerator()

	xcopy = x
	while xcopy > 1:
		prime_number = prime_iterator.next()
		if xcopy % prime_number == 0:
			xcopy /= prime_number
			prime_factors.append(prime_number)

		if prime_number > x:
			raise Exception('Lol')

	return prime_factors

class PrimeGenerator:
	def __init__(self):
		self.prime_entries = []
		self.generate_method = self.first

	def first(self):
		prime_number = None
		if len(self.prime_entries) == 0:
			prime_number = 2

		if len(self.prime_entries) == 1:
			prime_number = 3
			self.generate_method = self.iterative

		if prime_number:
			self.prime_entries.append(prime_number)
			return prime_number
		else:
			raise Exception('')

	def iterative(self):
		candidate = self.prime_entries[-1] + 2
		while True:
			for prime_number in self.prime_entries:
				if candidate % prime_number == 0:
					candidate += 2
					break
			else:
				self.prime_entries.append(candidate)
				return candidate

	def next(self):
		return self.generate_method()


if __name__ == '__main__':
	sample = 13195
	input = 600851475143

	print find_primes(sample)
	print max(find_primes(input))