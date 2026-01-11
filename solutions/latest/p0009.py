import logging

from solutions.euler.util.decorators import timed_function


def q9(perimeter=1000):
	"""
	"Brute force" method: we can bound c
	  - a + b + c = perimeter    # Rules of triangle
	  - a ^ 2 + b ^ 2 = c ^ 2    # Pythagoras

	c has to be bigger  than perimeter // 3 (because a + b + c = perimeter, and a < b < c)
	c has to be smaller than perimeter // 2 (otherwise, a and b cannot be big enough to be triangle)

	This is an introduction to Euclidean formula, but overkill for this question
	"""
	min_c, max_c = perimeter // 3, perimeter // 2
	logging.debug("min_c=%s, max_c=%s", min_c, max_c)

	for c in range(min_c, max_c + 1):
		min_a, max_a = perimeter - (2 * c) + 1, min(perimeter // 3, (perimeter - c) // 2)
		logging.debug("min_a=%s, max_a=%s", min_a, max_a)

		for a in range(min_a, max_a + 1):
			b = perimeter - a - c

			# Assumes only 1 solution, as given by the question
			if a * a + b * b == c * c:
				logging.info("S=%s::%s", perimeter, (a, b, c))
				return a * b * c

	raise ValueError("No solution found")


if __name__ == '__main__':
	import sys

	log_format = '[%(levelname)s] %(asctime)s (%(name)s) %(pathname)s:%(lineno)d::%(funcName)s - %(message)s'
	logging.basicConfig(stream=sys.stderr, level=logging.INFO, format=log_format)
	assert timed_function(q9)() == 31875000
