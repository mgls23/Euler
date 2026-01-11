"""
Problem 2: Even Fibonacci numbers (legacy NFibonacciIterator approach)
https://projecteuler.net/problem=2

Uses NFibonacciIterator.n3() to generate only even terms.
"""


def q2():
	from solutions.euler.maths.fibonacci import NFibonacciIterator
	from solutions.euler.strings.number_to_string import MILLION

	iterator = NFibonacciIterator.n3()
	iterator.set_upper_bound(4 * MILLION)

	return sum(iterator.sequence)


if __name__ == '__main__':
	result = q2()
	print(result)
