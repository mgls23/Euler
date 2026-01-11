"""
Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

Find the sum of all the multiples of 3 or 5 below 1000.

Solution uses Gaussian summation with inclusion-exclusion principle.
"""
from solutions.euler.maths.sigma import sigma_n


def _sigma_n_with_multiplier(upper_bound: int, multiples_of: int) -> int:
	"""Find sum of all multiples_of from 1 to upper bound.

	Taking the example of multiples_of=3:
	    3   +   6   +   9   +   12  +   ...   3n
	= (3x1) + (3x2) + (3x3) + (3x4) +   ... (3xn)
	= 3 x (1+2+3+ ... n)
	= 3 x sigma(1 -> n)
	= multiples_of * sigma(n)

	Args:
		upper_bound: Maximum value to consider
		multiples_of: The number to find multiples of

	Returns:
		Sum of all multiples up to upper_bound
	"""
	# Catch negative n cases as well as 0 case here
	if upper_bound < multiples_of: return 0
	return multiples_of * sigma_n(upper_bound // multiples_of)


def q1(upper_bound: int = 999) -> int:
	"""Calculate sum of multiples of 3 or 5 below upper_bound+1.

	Uses inclusion-exclusion: sum(3s) + sum(5s) - sum(15s)
	to avoid counting multiples of 15 twice.

	Args:
		upper_bound: Find multiples below this value (inclusive)

	Returns:
		Sum of all multiples of 3 or 5
	"""
	multiples_of_3 = _sigma_n_with_multiplier(upper_bound, 3)
	multiples_of_5 = _sigma_n_with_multiplier(upper_bound, 5)
	multiples_of_15 = _sigma_n_with_multiplier(upper_bound, 15)

	return (multiples_of_3 + multiples_of_5) - multiples_of_15


if __name__ == '__main__':
	print(q1())