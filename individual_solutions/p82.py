import logging

from euler.maths.matrix import debug_log_2d_matrix
from euler.util.decorators import timed_function
from euler.util.io import datafiles

NOT_CALCULATED = 2 ** 32 - 1  # Something arbitrarily big


def q82():
    cost_matrix = read_input_file()
    path_matrix = [
        [cost_matrix[y][0]] + [NOT_CALCULATED] * (len(cost_matrix[0]) - 1)
        for y in range(len(cost_matrix))
    ]

    debug_log_2d_matrix(path_matrix)
    for x in range(1, len(cost_matrix[0])):
        for y in range(len(cost_matrix)):
            cost = cost_matrix[y][x]
            existing_path = path_matrix[y][x]
            new_path = path_matrix[y][x - 1] + cost

            if new_path < existing_path:
                path_matrix[y][x] = new_path

                # Check Up
                for y_above in range(y - 1, 0 - 1, -1):
                    existing_path = path_matrix[y_above][x]
                    new_path = path_matrix[y_above + 1][x] + cost_matrix[y_above][x]
                    if new_path > existing_path: break
                    path_matrix[y_above][x] = new_path

                # Check Down
                for y_below in range(y + 1, len(cost_matrix)):
                    existing_path = path_matrix[y_below][x]
                    new_path = path_matrix[y_below - 1][x] + cost_matrix[y_below][x]
                    if new_path > existing_path: break
                    path_matrix[y_below][x] = new_path

    debug_log_2d_matrix(path_matrix)
    right_column = [path_matrix[y][-1] for y in range(len(path_matrix))]
    logging.debug(right_column)
    return min(right_column)


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
