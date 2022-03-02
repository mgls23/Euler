import re
import os
from math import floor

TOGGLE = True
UPPER_LIMIT = 5 if TOGGLE else 9


def string_to_2d_array(strings):
    return [[int(character) for character in line] for line in strings]


def get_block(integer):
    return int(floor(integer / 3))


class SudokuBlock:
    def __init__(self, cells, block_type, suffix):
        for cell in cells:
            setattr(cell, block_type, self)

        self.cells = cells
        self.block_type = block_type
        self.suffix = suffix

    def solved(self):
        return all(cell.solved() for cell in self.cells)

    def discard_possibility(self, value):
        for cell in self.cells:
            cell.discard_possibility(value)

    def check_if_solvable(self):
        counts = {i: (0, None) for i in range(1, 10)}

        for cell in self.cells:
            for possibility in cell.possibilities:
                counts[possibility] = counts[possibility][0] + 1, cell

        one_remaining = [(number, cell) for number, (count, cell) in counts.items() if count == 1]
        for number, cell in one_remaining:
            if all(getattr(cell, block_name).check_if_possible(number) for block_name in ('column', 'row', 'square')):
                print('X={}, Y={}, number={}'.format(str(self), cell.x, cell.y, number))
                cell.solve(number)

    def check_if_possible(self, value):
        return all(cell.value != value for cell in self.cells)

    def cells(self, solved=True):
        return [cell for cell in self.cells if cell.solved() == solved]

    def integrity_check(self):
        unique_cells = set()
        for cell in self.cells:
            for unique_cell in unique_cells:
                if cell.value == unique_cell.value:
                    raise Exception('{} and {} are the same!'.format(
                        cell, unique_cell
                    ))

            unique_cells.add(cell)

    def __str__(self):
        return '{} {}'.format(self.block_type, self.suffix)


class SudokuCell:
    """ Individual Cell that represents either a number or a list of possibilities
    of the given Sudoku Grid"""

    def __init__(self, solver, x, y, value=0):
        self.solver = solver
        self.x = x
        self.y = y

        self.value = value

        if self.solved():
            self.possibilities = set()
        else:
            self.possibilities = set(range(1, 9 + 1))

    def discard_possibility(self, possibility):
        if possibility in self.possibilities:
            self.possibilities.remove(possibility)
            self.check_if_solvable()

    def check_if_solvable(self):
        if len(self.possibilities) == 1:
            assert not self.solved(), ""
            value = self.possibilities.pop()
            self.solve(value)

    def solve(self, value):
        self.possibilities = []
        self.value = value
        self.solver.queue.append(self)

    def solved(self):
        return self.value != 0

    def string(self, debug=False):
        if debug and len(self.possibilities):
            if len(self.possibilities) == 9 and TOGGLE:
                return '*'

            elif len(self.possibilities) > UPPER_LIMIT:
                return '!' + str(','.join(str(i)
                    for i in set(range(1, 9 + 1)) - self.possibilities))

            return str('/'.join(str(i) for i in self.possibilities))

        return str(self.value or '-')

    def __str__(self):
        return self.string()

    def info(self):
        return '{}({},{})'.format(self.value, self.x, self.y)


class SudokuSolver:
    def __init__(self, grid=None):
        self.grid = [[
            SudokuCell(self, x, y, initial_value)
            for x, initial_value in enumerate(line)]
            for y, line in enumerate(grid)
        ]

        self.rows = [
            SudokuBlock(rows, 'row', str(y))
            for y, rows in enumerate(self.grid)
        ]

        self.columns = [
            SudokuBlock([row[y] for row in self.grid], 'column', str(y))
            for y, row in enumerate(self.grid)
        ]

        self.squares = []
        for y in [0, 3, 6]:
            row = []
            for x in [0, 3, 6]:
                square = []
                for i in range(3):
                    for j in range(3):
                        square.append(self.grid[x + i][y + j])

                row.append(SudokuBlock(square, 'square', '{},{}'.format(int(x / 3), int(y / 3))))

            self.squares.append(row)

        self.queue = []
        self.update()

    def update(self):
        self.queue = [
            cell for blocks in self.grid
            for cell in blocks if cell.solved()
        ]

    def solve(self):
        if not self.queue:
            print('\nQueue is empty')
            print(self.string(True))
            return

        print('Clear Queue')
        while self.queue:
            cell = self.queue.pop(0)

            print('\nGetting Rid of {}[{}, {}] Queue={}'.format(
                cell.value, cell.x, cell.y, [cell.info() for cell in self.queue]))
            print(self.string(True))

            self.rows[cell.y].discard_possibility(cell.value)
            self.columns[cell.x].discard_possibility(cell.value)

            # Cell iteration
            x_bound = get_block(cell.x)
            y_bound = get_block(cell.y)

            self.squares[x_bound][y_bound].discard_possibility(cell.value)

        if not self.solved():
            self.check_if_solvable(self.rows)
            self.check_if_solvable(self.columns)
            self.check_if_solvable([a for square in self.squares for a in square])
            self.solve()

    @staticmethod
    def check_if_solvable(blocks):
        for block in blocks:
            block.check_if_solvable()

    def string(self, debug=False):
        GRID = 5
        if debug:
            GRID = 12 if TOGGLE else 18

        strings = ['+' + '+'.join(['-' * (GRID * 3 + 2)] * 3) + '+']
        for index, blocks in enumerate(self.grid):
            strings += [
                '|' + '|'.join(block.string(debug).center(GRID) for block in blocks)
                + '|']

            if index % 3 == 2:
                strings += ['+' + '+'.join(['-' * (GRID * 3 + 2)] * 3) + '+']

        return '\n'.join(strings)

    def __str__(self):
        return self.string()

    def solved(self):
        return all(cell.solved() for line in self.grid for cell in line)

    def integrity_check(self):
        for blocks in (self.columns, self.rows, [cells for square in self.squares for cells in square]):
            for block in blocks:
                block.integrity_check()



SUFFIX = os.path.expanduser('~') + '/Projects/Euler/'


def q96():
    new_line_regex = re.compile('Grid ([0-9]*)')
    with open(SUFFIX + 'data/p096_sudoku.txt', 'r') as file:
        string_buffer = []
        last_match = None

        for line in file.readlines():
            new_line_match = new_line_regex.match(line)
            if new_line_match:
                if len(string_buffer):
                    array = string_to_2d_array(string_buffer)
                    solver = SudokuSolver(array)
                    solver.solve()

                    index, = last_match.groups()
                    print('\nGrid {}: {}'.format(index, solver.solved()))
                    print(str(solver) + '\n')
                    if not solver.solved():
                        return -1

                    if index == '00':
                        return -1

                string_buffer = []
                last_match = new_line_match
            else:
                string_buffer.append(line.strip('\n'))

    return -1


if __name__ == '__main__':
    q96()
