import logging
from itertools import accumulate
from typing import List

from solutions.euler.util.decorators import timed_function
from solutions.euler.util.io_utils import parse_matrix


def dijkstra_cost_search_fast(matrix: List[List[int]]):
	# Modifies the matrix given - call copy.deepcopy if this is undesired
	# logging.debug('Before')
	# debug_log_2d_matrix(matrix)

	# first row calculation
	matrix[0] = list(accumulate(matrix[0]))
	for r, row in enumerate(matrix[1:], 1):
		last_row = matrix[r - 1]

		# rather than in if statement, we handle first column and handle 1->
		row[0] += last_row[0]
		for c in range(1, len(matrix[0])):
			row[c] += min(row[c - 1], last_row[c])

	# logging.debug('After')
	# debug_log_2d_matrix(matrix)
	return matrix[-1][-1]


def dijkstra_cost_search(matrix: List[List[int]]):
	# Modifies the matrix given - call copy.deepcopy if this is undesired
	# logging.debug('Before')
	# debug_log_2d_matrix(matrix)

	# Boundary calculation
	for x in range(1, len(matrix[0])): matrix[0][x] += matrix[0][x - 1]
	for y in range(1, len(matrix)): matrix[y][0] += matrix[y - 1][0]

	# We can only call this once the boundary is done
	for y in range(1, len(matrix)):
		for x in range(1, len(matrix[y])):
			matrix[y][x] += min(matrix[y - 1][x], matrix[y][x - 1])

	# logging.debug('After')
	# debug_log_2d_matrix(matrix)
	return matrix[-1][-1]


def q81() -> int:
	return dijkstra_cost_search_fast(parse_matrix('p081_matrix.txt'))


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
	assert (timed_function(q81)() == 427337)
