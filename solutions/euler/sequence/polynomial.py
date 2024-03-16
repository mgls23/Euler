from solutions.euler.sequence.sequence import SequenceGenerator


class Polynomial(SequenceGenerator):
	def __init__(self, polynomial_degree):
		self.polynomial_degree = polynomial_degree

	def to_index(self, number):
		return number ** (1 / self.polynomial_degree)

	def to_number(self, index):
		return index ** self.polynomial_degree
