from solutions.euler.util.exceptions import NotSupportedException


class FibonacciIterator:
	""" A wrapper for Fibonacci sequence in case the requirement changes """

	def __init__(self, initial_list=None, start_with_two_1s=False):
		if initial_list is None:
			initial_list = start_with_two_1s and [1, 1] or [1, 2]

		self.sequence = initial_list

	def _calculate_next(self):
		return self.sequence[-1] + self.sequence[-2]

	def calculate_nth(self, n):
		"""Calculates and returns nth fibonacci sequence"""
		if n < 1:
			raise NotSupportedException('')

		# See if that value has been calculated already
		for _ in range(n - len(self.sequence)):
			self.sequence.append(self._calculate_next())

		# nth => n-1th in the list [0th of list is 1st Fibonacci]
		return self.sequence[n - 1]

	def set_upper_bound(self, upper_bound):
		if upper_bound < 1:
			raise NotSupportedException('')

		while self.sequence[-1] < upper_bound:
			self.sequence.append(self._calculate_next())

		# Discard any entries that are bigger than the upper bound
		while self.sequence[-1] > upper_bound:
			self.sequence.pop()

		# Return the last entry
		return self.sequence[-1]


class NFibonacciIterator(FibonacciIterator):
	"""Fibonacci Iterator that only contains nth progression

	Insight is that if we only want every nth member of the fibonacci sequence, we can
	save some calculation
	"""

	def __init__(self, every_nth, sequence, minus_1, minus_2):
		super(NFibonacciIterator, self).__init__(initial_list=sequence)
		self.every_nth = every_nth
		self.minus_1 = minus_1
		self.minus_2 = minus_2

	def _calculate_next(self):
		return self.sequence[-1] * self.minus_1 + self.sequence[-2] * self.minus_2

	@classmethod
	def n2(cls):
		""" For N2 case, specifically, this might actually slower (given that the 'saving' is additions,
			introduced calculation involves multiplication) However, this is demonstration of generic Fibonacci
			calculation that might allow us to save a fair amount when N becomes large

			If we consider :: n1, n2, n3, n4, n5
				n5 = n4 + n3 (Fibonacci Progression)
				n4 = n3 + n2 (Fibonacci Progression)

			A simple insight we will exploit is that we can also convert one of the smaller terms (i.e.)
				n4 = n5 - n3

			We are given n1 and n3. Let's convert n5 into n1 and n3s
				n5 = n4 + n3
				n5 = 2*n3 + n2           # Fibonacci replacement: n4 -> n3 + n2
				n2 = n3 - n1             # Fibonacci reordered:   n3 = n2 + n1

				n5 = 2*n3 + n2 = 3*n3 - n1

			the sequence can be simplified by multiplying the last entry by 3
			and subtracting the one before to obtain n5
			"""
		return NFibonacciIterator(every_nth=2, sequence=[2, 5], minus_1=3, minus_2=-1)

	@classmethod
	def n3(cls):
		"""
		n9  =           n8            +     n7
	        = (    n7    +     n6)    + (n6 + n5)
	        = ((n6 + n5) + (n5 + n4)) + (n6 + n5)
	        = 3*n6 + 2*n5

        n5  = n4 + n3
        n5  = n6 - n4
		2n5 = n6 + n3

		n9  = 4*n6 + n3
		"""
		return NFibonacciIterator(every_nth=3, sequence=[2, 8], minus_1=4, minus_2=1)
