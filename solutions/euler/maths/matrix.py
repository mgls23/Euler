import logging

import numpy


def adjacent_multiplicand_string(input_string, window_size):
	return adjacent_multiplicand(list(map(int, input_string)), window_size)


def adjacent_multiplicand(list_, window_size):
	y = list_[:-1]

	for iteration_count in range(1, window_size):
		for index in range(len(y) - 1):
			y[index] *= list_[index + iteration_count]

		y.pop(-1)

	return max(y)


def horizontal(matrix):
	return numpy.array(matrix).transpose().tolist()


def left_diagonal(matrix):
	return numpy.array([[0] * i + row + [0] * (len(matrix) - i) for i, row in enumerate(matrix)]).transpose().tolist()


def right_diagonal(matrix):
	return numpy.array([[0] * (len(matrix) - i) + row + [0] * i for i, row in enumerate(matrix)]).transpose().tolist()


def debug_log_2d_matrix(matrix):
	for row in matrix:
		logging.debug(f'{row}')
