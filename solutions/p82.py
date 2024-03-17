import logging

from solutions.euler.maths.matrix import debug_log_2d_matrix
from solutions.euler.util.decorators import timed_function
from solutions.euler.util.io_utils import datafiles

NOT_CALCULATED = 2 ** 32 - 1  # Something arbitrarily big


class CostNode:
	def __init__(self, cost, path=NOT_CALCULATED):
		self.cost = cost
		self.path = path
		self.listeners = []

	def add_connection(self, node):
		self.listeners.append(node)

	def check_with(self, new_path_before):
		new_path = new_path_before + self.cost
		if new_path < self.path:
			self.path = new_path
			for listener_node in self.listeners:
				listener_node.check_with(new_path)

	def __str__(self):
		return str(self.path)


def object_oriented_approach():
	# Uses linked lists to represents nodes to be updated
	cost_matrix = read_input_file()
	nodes = []
	for y in range(len(cost_matrix)):
		nodes.append([CostNode(cost=cost_matrix[y][0], path=cost_matrix[y][0])]
		             + [CostNode(cost=cost_matrix[y][x]) for x in range(1, len(cost_matrix[0]))])

	# The node above is a listener to node below
	for y in range(1, len(nodes)):
		for x in range(len(nodes[y])):
			nodes[y - 1][x].add_connection(nodes[y][x])

	# The node below is a listener to node above
	for y in range(len(nodes) - 1):
		for x in range(len(nodes[y])):
			nodes[y][x].add_connection(nodes[y + 1][x])

	# Check the direct connections
	for x in range(1, len(cost_matrix[0])):
		for y in range(len(cost_matrix)):
			nodes[y][x].check_with(nodes[y][x - 1].path)

	for row in nodes:
		logging.debug(', '.join(map(str, row)))

	right_column = [nodes[y][-1].path for y in range(len(nodes))]
	logging.debug(right_column)
	return min(right_column)


def traditional_approach():
	# runs within 98 milliseconds ish
	cost_matrix = read_input_file()
	path_matrix = [
		[cost_matrix[y][0]] + [NOT_CALCULATED] * (len(cost_matrix[0]) - 1)
		for y in range(len(cost_matrix))
	]

	debug_log_2d_matrix(path_matrix)
	for x in range(1, len(cost_matrix[0])):
		for y in range(len(cost_matrix)):
			new_path = path_matrix[y][x - 1] + cost_matrix[y][x]

			if new_path < path_matrix[y][x]:
				path_matrix[y][x] = new_path

				# Check Up
				for y_above in range(y - 1, 0 - 1, -1):
					new_path = path_matrix[y_above + 1][x] + cost_matrix[y_above][x]
					if new_path > path_matrix[y_above][x]: break
					path_matrix[y_above][x] = new_path

				# Check Down
				for y_below in range(y + 1, len(cost_matrix)):
					new_path = path_matrix[y_below - 1][x] + cost_matrix[y_below][x]
					if new_path > path_matrix[y_below][x]: break
					path_matrix[y_below][x] = new_path

	debug_log_2d_matrix(path_matrix)
	right_column = [path_matrix[y][-1] for y in range(len(path_matrix))]
	logging.debug(right_column)
	return min(right_column)


def q82():
	return object_oriented_approach()


def read_input_file():
	# Duplication of p81
	with open(datafiles('p082_matrix.txt')) as file:
		raw_input = file.readlines()
		matrix_string = [line.replace('\n', '').split(',') for line in raw_input]
		return [[int(element) for element in row] for row in matrix_string]


if __name__ == '__main__':
	import sys

	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert (timed_function(q82)() == 260324)
