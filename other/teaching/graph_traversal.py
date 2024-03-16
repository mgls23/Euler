from collections import defaultdict


def convert_into_graph(connections):
	graph = defaultdict(lambda: defaultdict(int))
	for u, v, w in connections: graph[u][v] = w
	return graph


def shorted_path_faster_algorithm(connections, number_of_nodes, starting_node):
	graph = convert_into_graph(connections)

	distances = [-1] + [float('inf') for _ in range(number_of_nodes)]
	distances[starting_node] = 0

	visited = [True] + [False for _ in range(number_of_nodes)]
	visited[starting_node] = True

	queue = [starting_node]
	while queue:
		source = queue.pop()
		for destination, weight in graph[source].items():
			new_path = distances[source] + weight
			if new_path < distances[destination]:
				distances[destination] = new_path
				if not visited[destination]:
					queue.append(destination)
					visited[destination] = True

	if all(visited):
		return max(distances[1:])
	else:
		return -1


def dijkstra(connections, number_of_nodes, start_node):
	graph = convert_into_graph(connections)

	distances = [-1] + [float('inf') for _ in range(number_of_nodes)]

	queue = [start_node] + list(range(1, start_node + 1))
	queue.pop(start_node)

	while queue:
		queue.sort(key=lambda remaining_node: distances[remaining_node])
		best_candidate = queue.pop(0)
		for destination, weight in graph[best_candidate]:
			new_path = distances[best_candidate] + weight
			distances[destination] = min(distances[destination], new_path)


print(shorted_path_faster_algorithm(
	[[4, 2, 76], [1, 3, 79], [3, 1, 81], [4, 3, 30], [2, 1, 47], [1, 5, 61], [1, 4, 99], [3, 4, 68], [3, 5, 46],
	 [4, 1, 6],
	 [5, 4, 7], [5, 3, 44], [4, 5, 19], [2, 3, 13], [3, 2, 18], [1, 2, 0], [5, 1, 25], [2, 5, 58], [2, 4, 77],
	 [5, 2, 74]],
	5,
	3)
)
