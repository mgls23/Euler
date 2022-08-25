import numpy


class Vector:
    def __init__(self, *elements):
        self._array = numpy.array(elements)

    def dot_product(self, other):
        # noinspection PyProtectedMember
        return self._array * other._array

    def distance(self):
        # Pythagoras
        return sum(map(lambda x: x ** 2, self._array))


def calculate_scalar_project(vector, vector_onto):
    dot_product = vector.dot_product(vector_onto)
    scalar_projection = dot_product / vector.distance()

    return scalar_projection


def calculate_change_in_basis(original_vector, *basis):
    length = len(original_vector)
