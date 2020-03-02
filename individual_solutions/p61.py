from abc import abstractmethod
from collections import deque
from itertools import combinations, permutations
from math import ceil

from euler.util.decorators import timed_function


class PolynomialSequence:
    polynomial_degree = 0

    @staticmethod
    @abstractmethod
    def to_number(index): pass

    @staticmethod
    @abstractmethod
    def to_index(number): pass

    @classmethod
    def generate_in_range(cls, digit=4):
        lower_bound = 10 ** (digit - 1)
        upper_bound = 10 ** digit

        lower_index = ceil(cls.to_index(lower_bound))
        upper_index = int(cls.to_index(upper_bound))

        return list(map(cls.to_number, range(lower_index, upper_index)))


class TriangleNumbers(PolynomialSequence):
    polynomial_degree = 3

    @staticmethod
    def to_number(index):
        return index * (index + 1) // 2

    @staticmethod
    def to_index(number):
        return ((8 * number + 1) ** 0.5 - 1) / 2


class SquareNumbers(PolynomialSequence):
    polynomial_degree = 4

    @staticmethod
    def to_number(index):
        return index ** 2

    @staticmethod
    def to_index(number):
        return number ** 0.5


class Pentagonal(PolynomialSequence):
    polynomial_degree = 5

    @staticmethod
    def to_number(index):
        return index * (3 * index - 1) // 2

    @staticmethod
    def to_index(number):
        return ((24 * number + 1) ** 0.5 + 1) / 6


class Hexagonal(PolynomialSequence):
    polynomial_degree = 6

    @staticmethod
    def to_number(index):
        return index * (2 * index - 1)

    @staticmethod
    def to_index(number):
        return ((8 * number + 1) ** 0.5 + 1) / 4


class Heptagonal(PolynomialSequence):
    polynomial_degree = 7

    @staticmethod
    def to_number(index):
        return index * (5 * index - 3) // 2

    @staticmethod
    def to_index(number):
        return ((40 * number + 9) ** 0.5 + 3) / 10


class Octagonal(PolynomialSequence):
    polynomial_degree = 8

    @staticmethod
    def to_number(index):
        return index * (3 * index - 2)

    @staticmethod
    def to_index(number):
        return ((3 * number + 1) ** 0.5 + 1) / 3


class FoundCyclicalException(Exception):
    pass


class PolynomialNode:
    def __init__(self, polynomial_type, number):
        self.polynomial_type = polynomial_type
        self.number = number

        number_string = str(number)
        self.prefix = number_string[:len(number_string) // 2]
        self.suffix = number_string[len(number_string) // 2:]

        self.connected = []

    def add_connection(self, node):
        if self.suffix == node.prefix:
            self.connected.append(node)

    def __str__(self):
        return f'[{self.polynomial_type}]({self.number})'

    def can_form_cycle_with(self, path):
        if all(self.polynomial_type != node.polynomial_type for node in path):
            if len(path) == 5:
                if path[0].prefix == self.suffix:
                    raise FoundCyclicalException
                else:
                    return False
            return True
        return False


def break_down(polynomial_type, digits):
    numbers = polynomial_type.generate_in_range(digits)

    broken_down = []
    for number in numbers:
        broken_down.append(PolynomialNode(polynomial_type.polynomial_degree, number))

    return broken_down


def q61(digits=4):
    triangular_numbers = break_down(TriangleNumbers, digits)
    square_numbers = break_down(SquareNumbers, digits)
    pentagonal_numbers = break_down(Pentagonal, digits)

    hexagonal_numbers = break_down(Hexagonal, digits)
    heptagonal_numbers = break_down(Heptagonal, digits)
    octagonal_numbers = break_down(Octagonal, digits)

    all_polynomials = [triangular_numbers, square_numbers, pentagonal_numbers, hexagonal_numbers,
                       heptagonal_numbers, octagonal_numbers]

    for collection1, collection2 in permutations(all_polynomials, 2):
        for node1 in collection1:
            for node2 in collection2:
                node1.add_connection(node2)

    paths = deque([([node], node) for node in all_polynomials[0]])
    while paths:
        path, last_node_in_path = paths.pop()
        for connected_node in last_node_in_path.connected:
            try:
                if connected_node.can_form_cycle_with(path):
                    paths.append((path + [connected_node], connected_node))
            except FoundCyclicalException:
                return sum([node.number for node in path + [connected_node]])


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(TriangleNumbers.to_index)(10 ** 3) == 44.224154547626725)

    assert (timed_function(q61)() == 28684)
