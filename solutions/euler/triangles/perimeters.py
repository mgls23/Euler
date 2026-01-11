import logging


def sieve_of_factors(upper_bound: int):
	factors = [set() for _ in range(upper_bound + 1)]

	# For 2s
	factors[2::2] = [{2} for _ in range(upper_bound // 2)]

	# For everything else
	for number in range(3, upper_bound + 1, 2):
		if not factors[number]:
			for other in range(number, upper_bound + 1, number):
				factors[other].add(number)

	return factors


def generate_coprime_pairs(upper_bound: int):
	factors = sieve_of_factors(upper_bound)
	for m in range(upper_bound):
		for n in range(1, m):
			if n not in factors[m]:
				yield m, n


def pythagorean_triplet_under(perimeter: int) -> list[tuple[int, int, int]]:
	"""
	Generates all Pythagorean triplets with given perimeter using Euclidean formula

	a = m ^ 2 - n ^ 2
	b = 2mn
	c = m ^ 2 + n ^ 2

	Parameters:
	    perimeter: int
	        Perimeter of a triangle is a + b + c (sum of all sides)

	Returns:
	   All Pythagorean triplets tuple[int], (a, b, c)
	"""
	primitive_triples, all_triples = set(), list()

	for m, n in generate_coprime_pairs(upper_bound=int(perimeter ** 0.5) + 1):
		if 1 != (number_of_odd := len(list(filter(lambda x: x % 2 == 0, (m, n))))):
			continue

		a = m * m - n * n
		b = 2 * m * n
		c = m * m + n * n

		# assert a * a + b * b == c * c
		for k in range(1, (perimeter // (a + b + c)) + 1):
			if k == 1:
				logging.info("Primitive Triplet: %s, m,n= %s", (a, b, c), (m, n))
				primitive_triples.add(tuple(sorted((a, b, c))))

			ka, kb, kc = k * a, k * b, k * c
			logging.info("  - %s", (ka, kb, kc))
			if (ka + kb + kc) <= perimeter:
				all_triples.add(tuple(sorted((ka, kb, kc))))

	return all_triples
