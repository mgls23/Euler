import bisect
import logging
from operator import itemgetter

import networkx as nx
import numpy as np

from solutions.euler.util.decorators import timed_function
from solutions.euler.util.graph_utils import adjacency_matrix_to_graph
from solutions.euler.util.io_utils import datafiles

NOT_EDGE = -1


def p107_graph() -> nx.Graph:
	matrix = np.genfromtxt(
		datafiles("0107_network.txt"),
		delimiter=',',
		missing_values="-",  # this is no edge in txt
		filling_values=NOT_EDGE,  # this is no edge in our data structure
		dtype='int16',
	)

	assert not np.any(matrix < NOT_EDGE), "dtype might be incorrect"
	return adjacency_matrix_to_graph(matrix, is_valid_edge=lambda x, y: matrix[x, y] != NOT_EDGE)


def sum_all_edges(graph: nx.Graph):
	return sum(map(itemgetter(2), graph.edges(data='weight')))


def prims_algorithm(graph: nx.Graph) -> nx.Graph:
	""" Prims Algorithm """
	min_span_tree = nx.Graph()

	next_edges = sorted(graph.edges(0, data='weight'), key=itemgetter(2))
	while len(min_span_tree.nodes) < len(graph.nodes):
		src_node, dst_node, weight = next_edges.pop(0)
		if dst_node in min_span_tree.nodes:
			logging.debug(f"Skipping {dst_node}, as it would create a cycle")
			continue

		min_span_tree.add_edge(src_node, dst_node, weight=weight)

		for new_edges in graph.edges(dst_node, data='weight'):
			bisect.insort(next_edges, new_edges, key=itemgetter(2))

	return min_span_tree


def solve_q107(graph: nx.Graph):
	mst_graph = prims_algorithm(graph)
	return sum_all_edges(graph) - sum_all_edges(mst_graph)


def q107():
	graph = p107_graph()
	return solve_q107(graph)


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q107)() == 259679)
