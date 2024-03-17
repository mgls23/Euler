import logging
import re
import sys
from collections import Counter

from solutions.euler.util.decorators import timed_function
from solutions.euler.util.io_utils import datafiles

ROW_SIZE = 3
COL_SIZE = 3
SQUARE_SIZE = ROW_SIZE * COL_SIZE

VALID_NUMBERS = set(range(1, SQUARE_SIZE + 1))


class Solver:
	def __init__(self, board: list[list[int]]):
		self.board = board
		self.check_board(validate_function=Solver.check_is_valid)

		self.numbers_in_row = list(map(set, self.rows))
		self.numbers_in_col = list(map(set, self.cols))
		self.numbers_in_square = list(map(set, self.squares))

		self.remaining_squares = sum(row.count(0) for row in self.board)

	@property
	def rows(self):
		return self.board

	@property
	def cols(self):
		return [[row[col] for row in self.board] for col in range(SQUARE_SIZE)]

	@property
	def squares(self):
		all_squares = [list() for _ in range(SQUARE_SIZE)]

		for row_index in range(9):
			for col_index in range(9):
				square_index = Solver.to_square_index(row_index, col_index)
				all_squares[square_index].append(self.board[row_index][col_index])

		return all_squares

	@staticmethod
	def to_square_index(row_index, col_index):
		return (row_index // 3) * 3 + col_index // 3

	def solve(self):
		if self.remaining_squares == 0:
			return True

		for row_index in range(9):
			for col_index in range(9):
				if self.board[row_index][col_index] == 0:
					for new_number in range(1, 9 + 1):
						square_index = Solver.to_square_index(row_index, col_index)
						if new_number in self.numbers_in_col[col_index] or new_number in self.numbers_in_row[row_index] \
								or new_number in self.numbers_in_square[square_index]:
							continue

						# logging.debug(f'Adding: ({row_index}, {col_index} / {square_index}) -> {new_number}')
						# logging.debug(self.taken_squares)
						# logging.debug(self.string())

						self.board[row_index][col_index] = new_number
						self.numbers_in_row[row_index].add(new_number)
						self.numbers_in_col[col_index].add(new_number)
						self.numbers_in_square[square_index].add(new_number)
						self.remaining_squares -= 1

						if self.solve():
							return True

						# logging.debug(f'Removing: ({row_index}, {col_index} / {square_index}) <- {new_number}')
						# logging.debug(self.taken_squares)
						# logging.debug(self.string())

						self.board[row_index][col_index] = 0
						self.numbers_in_row[row_index].remove(new_number)
						self.numbers_in_col[col_index].remove(new_number)
						self.numbers_in_square[square_index].remove(new_number)
						self.remaining_squares += 1

					return False

	def top_3_digit(self):
		""" Only for the purpose of q96 """
		return int(''.join(map(str, self.board[0][:3])))

	@staticmethod
	def check_is_solved(iterable):
		""" Row, Column, Squares are solve correctly if they have 9 unique elements """
		return set(iterable) == VALID_NUMBERS

	@staticmethod
	def check_is_valid(iterable):
		""" Row, Column, Squares are all valid if they have unique elements """
		counter = Counter(iterable)
		del counter[0]

		only_contains_valid_numbers = not (set(counter.keys()) - VALID_NUMBERS)
		only_occurs_once = all(occurrence == 1 for occurrence in counter.values())

		return only_contains_valid_numbers and only_occurs_once

	def check_board(self, validate_function=check_is_solved):
		""" Solved != Valid. This checks if the board is actually solved properly """
		for iterables, iterable_name in [(self.rows, 'Rows'), (self.cols, 'Cols'), (self.squares, 'Squares')]:
			for index, iterable in enumerate(iterables):
				if not validate_function(iterable):
					logging.error(f'Invalid {iterable_name}, Index: {index}')
					logging.error(f'Board\n{self.pretty_string()}')
					logging.error(f'Iterable: {iterable}')
					assert False, 'Invalid Board'

	@staticmethod
	def from_string(lines_read):
		return Solver([[int(element) for element in line.rstrip()] for line in lines_read if line])

	def pretty_string(self):
		cell_width = 7

		string_output = ['+' + '+'.join(['-' * (cell_width * 3 + 2)] * 3) + '+']
		for index, row in enumerate(self.board):
			string_output += ['|' + '|'.join(str(number).center(cell_width) for number in row) + '|']

			if index % 3 == 2:
				string_output += ['+' + '+'.join(['-' * (cell_width * 3 + 2)] * 3) + '+']

		return '\n'.join(string_output)


def q96():
	digit_sum = 0

	new_line_regex = re.compile('Grid ([0-9]+)')
	with open(datafiles('p096_sudoku.txt')) as file:
		grids = re.split(new_line_regex, file.read())[1:]
		sudoku_indices, sudoku_boards = grids[::2], grids[1::2]

		for index, board in enumerate(sudoku_boards):
			logging.info(f'Board {sudoku_indices[index]}')
			solver = Solver.from_string(board.split('\n'))

			# logging.debug('Before\n' + solver.pretty_string())
			solver.solve()
			solver.check_board()
			logging.debug('Solution\n' + solver.pretty_string())
			digit_sum += solver.top_3_digit()

	return digit_sum


if __name__ == '__main__':
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	assert timed_function(q96)() == 24702
