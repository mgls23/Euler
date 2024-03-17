import logging
from io import StringIO

import numpy as np

from solutions.euler.util.graph_utils import adjacency_matrix_to_graph
from solutions.euler.util.io_utils import remove_empty_lines_and_left_margin
from solutions.p107 import NOT_EDGE, solve_q107, sum_all_edges


def test_q107_example():
	example_str_raw = \
		"""
		- 16	12	21	-	-	-
		16	-	-	17	20	-	-
		12	-	-	28	-	31	-
		21	17	28	-	18	19	23
		-	20	-	18	-	-	11
		-	-	31	19	-	-	27
		-	-	-	23	11	27	-
		""".replace('\t', ' ')
	example_str = remove_empty_lines_and_left_margin(example_str_raw)
	adj_matrix = np.genfromtxt(
		StringIO(example_str),
		delimiter=' ',
		missing_values="-",  # this is no edge in txt
		filling_values=NOT_EDGE,  # this is no edge in our data structure
		dtype='int8',
	)
	graph = adjacency_matrix_to_graph(adj_matrix, is_valid_edge=lambda x, y: adj_matrix[x, y] != NOT_EDGE)

	assert sum_all_edges(graph) == 243
	assert solve_q107(graph) == 150


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	test_q107_example()
