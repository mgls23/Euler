import logging
import re
import sys
from itertools import permutations
from typing import List

from euler.util.io import datafiles

NOT_SOLVED = 0
SIZE = 9


class SolvedException(Exception):
    pass


class Solver:
    def __init__(self, board: List[List[int]]):
        self.board = board

    def solve(self):
        try:
            self._solve()

        except SolvedException:
            assert self.is_valid_sudoku(validate=Solver.check_is_solved_board)

    def _solve(self, fixed_row=0):
        if fixed_row == SIZE:
            raise SolvedException()

        row = self.board[fixed_row]
        already_in_row = set(row)
        numbers_missing = set(range(1, 10)) - already_in_row
        unsolved_indices = [index for index, number in enumerate(row) if number == 0]

        for permutation in permutations(numbers_missing):
            # Make changes
            for index, number in enumerate(permutation):
                row[unsolved_indices[index]] = number

            # Recurse
            if self.is_valid_sudoku(Solver.check_is_valid):
                self._solve(fixed_row=fixed_row + 1)

            # Revert
            # No need as we are going to overwrite them again anyway

    def top_3_digit(self):
        return int(''.join(map(str, self.board[0][:3])))

    @staticmethod
    def check_is_valid(iterable):
        """ Valid != Solved, used to check if making a change / state is okay (currently - even if this move causes
        something down the line - it only checks it at this particular level) """
        encountered = set()
        for number in (element for element in iterable if element != NOT_SOLVED):
            if number in encountered: return False
            encountered.add(number)

        return True

    @staticmethod
    def check_is_solved_board(iterable):
        """ Solved != Valid. This checks if the board is actually solved """
        unique_elements = set(iterable)
        return len(unique_elements) == 9 and NOT_SOLVED not in unique_elements

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


def q96():
    digit_sum = 0

    new_line_regex = re.compile('Grid ([0-9]*)')
    with open(datafiles('p096_sudoku.txt')) as file:
        lines_read = []
        last_new_line_match = None

        for line in file.readlines():
            if new_line_match := new_line_regex.match(line):
                if last_new_line_match:
                    sudoku_index, = last_new_line_match.groups()
                    logging.debug(f'Solving {sudoku_index}...')
                    solver = Solver.from_string(lines_read)
                    solver.solve()
                    digit_sum += solver.top_3_digit()

                last_new_line_match = new_line_match
                lines_read.clear()
            else:
                lines_read.append(line)

    return digit_sum


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q96())
