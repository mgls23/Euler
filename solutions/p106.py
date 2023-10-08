import logging


def meta_testing(a: list):
	a.sort()

	max_len = len(a) // 2
	b, c = [], []
	comparison = 0

	def helper(i=0):
		if 1 < len(b) == len(c):
			big_small = set(e1 < e2 for e1, e2 in zip(b, c))
			if big_small == {False, True}:
				nonlocal comparison
				logging.debug(f'Comparing::{b} and {c}')
				comparison += 1

		if len(b) < max_len:
			for j in range(i, len(a)):
				b.append(a[j])
				helper(j + 1)
				b.pop()

		if len(c) < max_len:
			for j in range(i, len(a)):
				# Remove duplicates by only making c[0] bigger than b[0] (a is sorted)
				# Even though it seems like we're adding potentially redundant if-statement in for-loop
				# This is better than the alternative of putting this at the beginning because we don't incur
				# list manipulation penalty (append and pop to c) and stack-call to another helper just to return
				if b and not c and b[0] < a[j]: continue

				c.append(a[j])
				helper(j + 1)
				c.pop()

	helper()
	return comparison


def q106(n=12):
	return meta_testing(list(range(1, n + 1)))


if __name__ == '__main__':
	import sys
	from .euler.util.decorators import timed_function

	# Logging adds on a lot of time
	# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q106)(n=7) == 70)
	assert (timed_function(q106)(n=12) == 21384)
