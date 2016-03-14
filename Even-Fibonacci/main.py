import argparse

N = 'N'


class FibonacciIterator:
	"""
		Special FibonacciIterator that skips the first 1 from conventional Fibonacci sequence

		(x) 1, 2, 3, 5, 8, 13, ...
		( ) 1, 1, 2, 3, 5, 8, 13, ...

	"""

	def __init__(self):
		self.calculated = []

	def next(self):
		if len(self.calculated) == 0:
			current_entry = 1

		elif len(self.calculated) == 1:
			current_entry = 2

		else:
			last_entry = self.calculated[-1]
			penultimate = self.calculated[-2]

			current_entry = last_entry + penultimate

		self.calculated.append(current_entry)
		return current_entry

	def next_jump(self, n=1):
		current_entry = None
		while n > 0:
			current_entry = self.next()
			n -= 1

		return current_entry


def naive_implementation(upper_bound):
	fibonacci_iterator = FibonacciIterator()
	# fibonacci_iterator.next()
	back_trace = []

	while True:
		# Because we only want even numbers, we would like to retain every second iteration
		current = fibonacci_iterator.next_jump(n=2)

		# If the value exceed the upper_bound, break the loop
		if current >= upper_bound:
			break

		# If
		back_trace.append(current)

	print back_trace

	# Return the sum of even Fibonacci Numbers
	cumulative = sum(back_trace)
	return cumulative


def better_solution(x):
	return -1


def configure_parser_and_extract():
	# Configure parser
	parser = argparse.ArgumentParser(description='Finds all the multiples of 3s and 5s below the given number')
	parser.add_argument(N, metavar='M', type=int, nargs='+', help='The number you wish to supply')

	# Parse the argument and extract the number to use in FizzBuzz
	args = parser.parse_args()

	# Return parsed arguments
	return args.N[0]


if __name__ == '__main__':
	# Configure Parser and extract upper bound we need
	upper_bound = configure_parser_and_extract()

	# Find the result
	result = naive_implementation(upper_bound)

	# Output the result
	print result
