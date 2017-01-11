import argparse

N = 'N'


class NotSupportedException(Exception):
	pass


class FibonacciIterator:
	""" FibonacciIterator that calculates and stores calculated
    fibonacci sequence values. N.B. This excludes the 1st 1

		(x) 1, 2, 3, 5, 8, 13, ...
		( ) 1, 1, 2, 3, 5, 8, 13, ...
	"""

	def __init__(self, *args):
		self._sequence = list(args)

	def _calculate_next_(self):
		"""Calculates and stores the next Fibonacci Sequence"""
		self._sequence.append(self._sequence[-1] + self._sequence[-2])

	def calculate_nth_fibonacci(self, n):
		"""Calculates and returns nth fibonacci sequence"""
		if n < 1:
			raise NotSupportedException('')

		# See if that value has been calculated already
		while len(self._sequence) < n:
			self._calculate_next_()

        # nth => n-1th in the list [0th of list is 1st Fibonnaci]
		return self._sequence[n - 1]

	def peek(self):
		"""Returns and shows the last entry of the fibonacci sequence

			Returns
			-------
			The last fibonacci sequence generated
		"""
		return self._sequence[-1]

	def back_trace(self):
		return self._sequence[:]

	def set_upper_bound(self, upper_bound):
		if upper_bound < 1:
			raise NotSupportedException('')

		while self.peek() < upper_bound:
			self._calculate_next_()

		# Discard any entries that are bigger than the upper bound
		while self.peek() > upper_bound:
			self._sequence.pop(-1)

		# Return the last entry
		return self.peek()


class NFibonacciIterator(FibonacciIterator):
	"""
		Fibonacci Iterator that only contains nth progression

		For example, for N=3

		     (x)       (x)
		1, 2, 3, 5, 8, 13, ...
		      N        2N
	"""

	def __init__(self, N=1, offset=0, fib_generator=FibonacciIterator(1, 2)):
		FibonacciIterator.__init__(
				self,
				fib_generator.calculate_nth_fibonacci(N + offset),
				fib_generator.calculate_nth_fibonacci(N * 2 + offset),
		)
		self.prev = fib_generator.calculate_nth_fibonacci(N * 2 - 1 + offset)
		self.N = N
		self.offset = offset

	def _calculate_next_(self):
		# Create a new iterator with the saved term and the new
		iterator = FibonacciIterator(self.prev, self._sequence[-1])

		# Update the entries and previous
		self.prev = iterator.calculate_nth_fibonacci(self.N * 2 - 1 + self.offset)
		self._sequence.append(iterator.calculate_nth_fibonacci(self.N * 2 + self.offset))


class N2FibonacciIterator(FibonacciIterator):
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
		FibonacciIterator.__init__(self, 2, 5)

	def _calculate_next_(self):
		self._sequence.append(self._sequence[-1] * 3 - self._sequence[-2])


def configure_parser_and_extract():
	# Configure parser
	parser = argparse.ArgumentParser(description='Finds all the multiples of 3s and 5s below the given number')
	parser.add_argument(N, metavar='M', type=int, nargs='+', help='The number you wish to supply')

	# Parse the argument and extract the number to use in FizzBuzz
	args = parser.parse_args()

	# Return parsed arguments
	return args.N[0]


def run():
    # Configure Parser and extract upper bound we need
    upper_bound = configure_parser_and_extract()

    #
    fib_generator = FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    back_trace = [(index, x) for index, x in
                  enumerate(fib_generator.back_trace()) if x % 2 == 0]

    #
    fib_generator = N2FibonacciIterator()
    fib_generator.set_upper_bound(upper_bound)
    back_trace = fib_generator.back_trace()
    answer = sum(back_trace)

    print back_trace
    print answer

if __name__ == '__main__':
    run()