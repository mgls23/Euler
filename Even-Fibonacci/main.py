import argparse

N = 'N'


class OptimisedTwoJumpSumIterator:
	"""
		Examining the even iterating sequence, we could see that the nth term is actually the (n-1)th x 3 - (n-2)th
		If we consider :: x1, x2, x3, x4, x5
		We wish to derive x5. We have x1 and x3.
			x4 = x3 + x2 (Fibonacci Progression)
			x5 = x4 + x3 (Fibonacci Progression)
		Since we have x1 and x3, we want to express x5 in those terms, which is
			x4 + x3
			= 2x3 + x2

		Since we have
			x3 = x2 + x1
		We also have
			x2 = x3 - x1

		Therefore
			x5 = 2x3 + x2 = 3x3 - x1

		So, we can substitute the actual process by multiplying the last entry by 3 and subtracting the one before to
		obtain x5
	"""

	def __init__(self):
		self.calculate = [2, 5]

	def get(self, n):
		if self.calculate[-1] > n:
			offset = 2
			while self.calculate[offset] > n:
				offset += 1
				if offset > len(self.calculate):
					raise Exception('')

		while self.calculate[-1] < n:
			last_entry = self.calculate[-1]
			penultimate = self.calculate[-2]
			new_entry = last_entry * 3 - penultimate
			self.calculate.append(new_entry)

		return self.calculate[-1]


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
