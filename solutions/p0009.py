import logging


def q9_improved(perimeter=1000):
	min_c, max_c = perimeter // 3, perimeter // 2
	logging.debug("min_c=%s, max_c=%s", min_c, max_c)

	for c in range(min_c, max_c + 1):
		min_a, max_a = perimeter - (2 * c) + 1, min(perimeter // 3, (perimeter - c) // 2)
		logging.debug("min_a=%s, max_a=%s", min_a, max_a)

		for a in range(min_a, max_a + 1):
			b = perimeter - a - c

			if a * a + b * b == c * c:
				logging.info("S=%s::%s", perimeter, (a, b, c))
				return a * b * c

	raise ValueError("No solution found")


def q9_adapted_to_hackerrank(perimeter=1000):
	""" This approach times out because of the 2 for-loops (which makes the solution O(a * c))

	The improved version of this solution (accepted by HackerRank) can be found in online, explained in p009.ipynb
	"""
	if perimeter % 2 != 0:
		return -1

	max_multiplier = -1

	min_c, max_c = perimeter // 3, perimeter // 2
	logging.debug("min_c=%s, max_c=%s", min_c, max_c)

	for c in range(min_c, max_c + 1):
		min_a, max_a = perimeter - (2 * c) + 1, min(perimeter // 3, (perimeter - c) // 2)
		logging.debug("min_a=%s, max_a=%s", min_a, max_a)

		for a in range(min_a, max_a + 1):
			b = perimeter - a - c

			if a * a + b * b == c * c:
				logging.info("S=%s::%s", perimeter, (a, b, c))
				max_multiplier = max(max_multiplier, a * b * c)

	return max_multiplier


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


def euclid_formula(upper_bound):
	primitive_triples, all_triples = set(), set()

	for m, n in generate_coprime_pairs(upper_bound=int(upper_bound ** 0.5) + 1):
		if 1 != (number_of_odd := len(list(filter(lambda x: x % 2 == 0, (m, n))))):
			continue

		a = m * m - n * n
		b = 2 * m * n
		c = m * m + n * n

		# assert a * a + b * b == c * c
		for k in range(1, (upper_bound // (a + b + c)) + 1):
			if k == 1:
				logging.info("Primitive Triplet: %s, m,n= %s", (a, b, c), (m, n))
				primitive_triples.add(tuple(sorted((a, b, c))))

			ka, kb, kc = k * a, k * b, k * c
			logging.info("  - %s", (ka, kb, kc))
			if (ka + kb + kc) <= upper_bound:
				all_triples.add(tuple(sorted((ka, kb, kc))))

	return all_triples


if __name__ == '__main__':
	import sys

	log_format = '[%(levelname)s] %(asctime)s (%(name)s) %(pathname)s:%(lineno)d::%(funcName)s - %(message)s'
	logging.basicConfig(stream=sys.stderr, level=logging.INFO, format=log_format)
	# timed_function(test_q9)()
	assert timed_function(q9_improved)() == 31875000
	# print(list(generate_coprime_pairs(1, 100)))

	# print(euclid_formula(50))
