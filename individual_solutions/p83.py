import logging

from euler.util.decorators import timed_function
from euler.util.io import parse_matrix

NOT_CALCULATED = 2 ** 32 - 1  # Something arbitrarily big


def q83() -> int:
    matrix = parse_matrix('p083_matrix.txt')

    rows, cols = len(matrix), len(matrix[0])
    cost_matrix = [[NOT_CALCULATED for _ in range(cols)] for _ in range(rows)]

    cost_matrix[0][0] = matrix[0][0]
    queue = [(0, 0)]

    while queue:
        r, c = queue.pop()
        for r_offset, c_offset in [(0, 1), (1, 0)]:
            r_new, c_new = r + r_offset, c + c_offset
            if 0 <= r_new < rows and 0 <= c_new < cols:
                old_cost = cost_matrix[r_new][c_new]
                new_cost = cost_matrix[r][c] + matrix[r_new][c_new]
                if new_cost < old_cost:
                    queue.append((r_new, c_new))
                    cost_matrix[r_new][c_new] = new_cost

    return cost_matrix[-1][-1]


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    assert (timed_function(q83)() == 427337)
