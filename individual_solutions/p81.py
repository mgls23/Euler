from euler.util.decorators import timed_function


def debug_log_2d_matrix(matrix):
    for row in matrix:
        logging.debug(f'{row}')


def dijkstra_cost_search(matrix):
    # Modifies the matrix given - call copy.deepcopy if this is undesired
    logging.debug('Before')
    debug_log_2d_matrix(matrix)

    # Boundary calculation
    for x in range(1, len(matrix[0])): matrix[0][x] += matrix[0][x - 1]
    for y in range(1, len(matrix)): matrix[y][0] += matrix[y - 1][0]

    # We can only call this once the boundary is done
    for y in range(1, len(matrix)):
        for x in range(1, len(matrix[y])):
            matrix[y][x] += min(matrix[y - 1][x], matrix[y][x - 1])

    logging.debug('After')
    debug_log_2d_matrix(matrix)
    return matrix[-1][-1]


def q81():
    return dijkstra_cost_search(read_input_file())


def read_input_file():
    with open('../data/p081_matrix.txt') as file:
        raw_input = file.readlines()
        matrix_string = [line.replace('\n', '').split(',') for line in raw_input]
        return [[int(element) for element in row] for row in matrix_string]


if __name__ == '__main__':
    import logging

    # import sys
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q81)() == 427337)
