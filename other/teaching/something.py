number = int(input())
raw_inputs = [input() for _ in range(number)]
graph = {}
for raw_input in raw_inputs:
	start, destination = raw_input.split(':')
	graph[start] = list(destination)

min_lengths = {key: float('inf') for key in graph}
visited = set()
queue = [('I', 0)]
while queue:
	current_node, distance = queue.pop()
	print('visit:', current_node)
	for connected in graph[current_node]:
		if connected not in visited:
			min_lengths[connected] = min(min_lengths[connected], distance + 1)
			queue.append((connected, distance + 1))
			visited.add(current_node)

	print(min_lengths)
	print(queue)

print(max(min_lengths.values()))
