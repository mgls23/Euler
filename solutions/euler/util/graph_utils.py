import networkx as nx
import numpy as np

AdjacencyMatrix = np.array


def adjacency_matrix_to_graph(adj_matrix: AdjacencyMatrix, is_valid_edge=None) -> nx.Graph:
	if is_valid_edge is None:
		is_valid_edge = lambda x, y: not np.isnan(adj_matrix[x, y])

	graph = nx.Graph()

	# Add nodes and edges to the graph
	num_nodes = len(adj_matrix)
	graph.add_nodes_from(range(num_nodes))

	# Iterate through the adjacency matrix and add edges
	for node1 in range(num_nodes):
		for node2 in range(num_nodes):
			if is_valid_edge(node1, node2):
				graph.add_edge(node1, node2, weight=adj_matrix[node1, node2])

	return graph
