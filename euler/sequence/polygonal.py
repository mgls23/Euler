from abc import ABCMeta

from euler.sequence.sequence import Sequence


class Polygonal(Sequence, metaclass=ABCMeta):
    polygonal_degree: int


class Triangle(Polygonal):
    polygonal_degree = 3

    @staticmethod
    def to_number(index):
        return index * (index + 1) // 2

    @staticmethod
    def to_index(number):
        return ((8 * number + 1) ** 0.5 - 1) / 2


class Square(Polygonal):
    polygonal_degree = 4

    @staticmethod
    def to_number(index):
        return index ** 2

    @staticmethod
    def to_index(number):
        return number ** 0.5


class Pentagonal(Polygonal):
    polygonal_degree = 5

    @staticmethod
    def to_number(index):
        return index * (3 * index - 1) // 2

    @staticmethod
    def to_index(number):
        return ((24 * number + 1) ** 0.5 + 1) / 6


class Hexagonal(Polygonal):
    polygonal_degree = 6

    @staticmethod
    def to_number(index):
        return index * (2 * index - 1)

    @staticmethod
    def to_index(number):
        return ((8 * number + 1) ** 0.5 + 1) / 4


class Heptagonal(Polygonal):
    polygonal_degree = 7

    @staticmethod
    def to_number(index):
        return index * (5 * index - 3) // 2

    @staticmethod
    def to_index(number):
        return ((40 * number + 9) ** 0.5 + 3) / 10


class Octagonal(Polygonal):
    polygonal_degree = 8

    @staticmethod
    def to_number(index):
        return index * (3 * index - 2)

    @staticmethod
    def to_index(number):
        return ((3 * number + 1) ** 0.5 + 1) / 3
