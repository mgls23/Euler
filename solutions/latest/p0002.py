"""
Problem 2: Even Fibonacci numbers
https://projecteuler.net/problem=2

Sum the even-valued Fibonacci terms not exceeding four million.

Use the recurrence for even terms: E(n) = 4*E(n-1) + E(n-2).
"""
import logging


def q2(upper_bound: int = 4_000_000) -> int:
	"""Sum even Fibonacci numbers up to upper_bound (inclusive)."""
	if upper_bound < 2:
		return 0

	# Even Fibonacci terms: 2, 8, 34, ...
	prev, curr = 2, 8
	total = 2
	while curr <= upper_bound:
		total += curr
		prev, curr = curr, 4 * curr + prev

	return total


if __name__ == '__main__':
	from solutions.euler.util.runner import run_solution

	run_solution(q2, 2)
