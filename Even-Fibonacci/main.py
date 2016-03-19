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


class NotSupportedException(Exception):
	pass


class FibonacciIterator:
	"""
		FibonacciIterator that calculates and stores fibonacci sequence values. N.B. This excludes the 0th 1

		(x) 1, 2, 3, 5, 8, 13, ...
		( ) 1, 1, 2, 3, 5, 8, 13, ...

	"""

	def __init__(self):
		self.sequence = [1, 2]

	def __calculate_next__(self):
		"""
		Calculates and stores the next Fibonacci Sequence
		"""
		self.sequence.append(self.sequence[-1] + self.sequence[-2])

	def get_nth_fibonacci(self, n):
		"""
		Calculates and returns nth fibonacci sequence

		Parameters
		----------
		n

		Returns
		-------

		"""
		#
		if n < 1:
			raise NotSupportedException('')

		# There is no need to recalculate a fibonacci value that has already been calculated
		while len(self.sequence) < n:
			self.__calculate_next__()

		# Return the last entry
		return self.sequence[n - 1]

	def peek(self):
		return self.sequence[-1]

	def calculate_with_upper_bound(self, upper_bound):
		pass


class NFibonacciIterator(FibonacciIterator):
	"""
		Fibonacci Iterator that only contains nth progression

		For example, for N=3
		(x)     (x)
		1, 2, 3, 5, 8, 13, ...
	"""

	def __init__(self, N=1):
		FibonacciIterator.__init__(self)
		self.n = N
		self.before = []
		self.after = []

	def calculate_next(self):
		pass


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
	result = NFibonacciIterator(N=2).get_nth_fibonacci(upper_bound)

	# Output the result
	print result
