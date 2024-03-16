import logging
from bisect import insort

from solutions.euler.util.decorators import timed_function
from solutions.euler.util.io import parse_matrix

NOT_CALCULATED = 2 ** 32 - 1  # Something arbitrarily big


def q83() -> int:
	matrix = parse_matrix('p083_matrix.txt')

	rows, cols = len(matrix), len(matrix[0])
	cost_matrix = [[NOT_CALCULATED for _ in range(cols)] for _ in range(rows)]

	queue = [(0, 0, 0)]
	while queue:
		r, c, cost_so_far = queue.pop()

		new_cost = cost_so_far + matrix[r][c]
		if new_cost >= cost_matrix[r][c]: continue

		cost_matrix[r][c] = new_cost
		if r == rows - 1 and c == cols - 1: break

		for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			r_new, c_new = r + r_offset, c + c_offset
			if 0 <= r_new < rows and 0 <= c_new < cols \
					and new_cost + matrix[r_new][c_new] < cost_matrix[r_new][c_new]:  # unnecessary, but worthwhile speedup

				# maintain a priority queue such that we investigate the most likely candidate first
				# insort because we can binary-insert the quickest
				insort(queue, (r_new, c_new, new_cost), key=lambda tuple_: -tuple_[2])

	return cost_matrix[-1][-1]


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
	assert (timed_function(q83)() == 425185)
