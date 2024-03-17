import networkx as nx
from matplotlib import pyplot as plt


def graph_to_image(graph: nx.Graph, title: str = ''):
	plt.figure(figsize=(len(graph.nodes), len(graph.nodes)))

	pos = nx.spring_layout(graph)
	nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=700)
	nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))

	plt.title(title)
	plt.show()
