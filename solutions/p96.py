import logging
import re
import sys
from typing import List, Set

from euler.util.decorators import timed_function
from euler.util.io import datafiles

NOT_SOLVED = 0
SIZE = 9


class SolvedException(Exception):
    pass


class Solver:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.taken_rows = [set(row) for row in self.board]
        self.taken_cols = [{row[col] for row in self.board} for col in range(9)]

        # Slightly different to make list slicing slightly more efficient
        self.taken_squares: List[Set[int]] = [set() for _ in range(9)]
        for row_index, row in enumerate(self.board):
            for col_index in range(3):
                self.taken_squares[(row_index // 3) * 3 + col_index].update(row[col_index * 3: (col_index + 1) * 3])

        self.remaining_squares = sum(row.count(0) for row in self.board)

    def solve(self):
        if self.remaining_squares == 0: return True

        for row_index in range(9):
            for col_index in range(9):
                if self.board[row_index][col_index] == 0:
                    for new_number in range(1, 9 + 1):
                        square_index = Solver.to_square_index(row_index, col_index)
                        if new_number in self.taken_cols[col_index] or new_number in self.taken_rows[row_index] \
                                or new_number in self.taken_squares[square_index]:
                            continue

                        # logging.debug(f'Adding: ({row_index}, {col_index} / {square_index}) -> {new_number}')
                        # logging.debug(self.taken_squares)
                        # logging.debug(self.string())

                        self.board[row_index][col_index] = new_number
                        self.taken_rows[row_index].add(new_number)
                        self.taken_cols[col_index].add(new_number)
                        self.taken_squares[square_index].add(new_number)
                        self.remaining_squares -= 1

                        if self.solve(): return True

                        # logging.debug(f'Removing: ({row_index}, {col_index} / {square_index}) <- {new_number}')
                        # logging.debug(self.taken_squares)
                        # logging.debug(self.string())

                        self.board[row_index][col_index] = 0
                        self.taken_rows[row_index].remove(new_number)
                        self.taken_cols[col_index].remove(new_number)
                        self.taken_squares[square_index].remove(new_number)
                        self.remaining_squares += 1

                    return False

    def top_3_digit(self):
        # assert self.is_valid_sudoku(validate=Solver.check_is_solved_board)
        return int(''.join(map(str, self.board[0][:3])))

    @staticmethod
    def check_is_solved_board(iterable):
        """ Solved != Valid. This checks if the board is actually solved """
        unique_elements = set(iterable)
        return len(unique_elements) == 9 and NOT_SOLVED not in unique_elements

    @staticmethod
    def to_square_index(row_index, col_index):
        return (row_index // 3) * 3 + col_index // 3

    def is_valid_sudoku(self, validate):
        rows_are_good = all(validate(row) for row in self.board)
        cols_are_good = all(validate(row[col] for row in self.board) for col in range(9))

        squares = [[] for _ in range(9)]
        for row_index, row in enumerate(self.board):
            for col_index in range(3):
                squares[(row_index // 3) * 3 + col_index] += row[col_index * 3: (col_index + 1) * 3]

        squares_are_good = all(validate(square) for square in squares)
        return rows_are_good and cols_are_good and squares_are_good

    @staticmethod
    def from_string(lines_read):
        return Solver([[int(element) for element in line.rstrip()] for line in lines_read])

    def string(self):
        cell_width = 7

        string_output = ['+' + '+'.join(['-' * (cell_width * 3 + 2)] * 3) + '+']
        for index, row in enumerate(self.board):
            string_output += ['|' + '|'.join(str(block).center(cell_width) for block in row) + '|']

            if index % 3 == 2:
                string_output += ['+' + '+'.join(['-' * (cell_width * 3 + 2)] * 3) + '+']

        return '\n'.join(string_output)


@timed_function
def q96():
    digit_sum = 0

    new_line_regex = re.compile('Grid ([0-9]*)')
    with open(datafiles('p096_sudoku.txt')) as file:
        lines_read = []
        for line in file.readlines():
            if new_line_regex.match(line):
                if lines_read:
                    # logging.debug(f'Solving {sudoku_index}...')
                    solver = Solver.from_string(lines_read)
                    solver.solve()
                    # logging.debug('Solution\n' + solver.string())
                    digit_sum += solver.top_3_digit()

                lines_read.clear()
            else:
                lines_read.append(line)

    return digit_sum


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q96())
