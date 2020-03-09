from math import sqrt

import sympy

from euler.maths.prime import generate_to_sie
from euler.util.decorators import timed_function


def find_minimal_x(d):
    if sqrt(d).is_integer():
        return -1, -1

    for y in range(1, 50000):
        x_squared = d * (y ** 2) + 1
        x = sqrt(x_squared)
        if x.is_integer():
            return int(x), y
    return -2, -2


def investigate(number=1000):
    max_x = 0
    for d in range(2, number):
        x, y = find_minimal_x(d)
        if x > max_x or x == -2:
            print(f'd={d}, find_y={(x, y)}')
        max_x = max(max_x, x)

    return max_x


def investigate2(number=1000):
    for x in range(100000):
        factorised = sympy.factorint(x ** 2 - 1)
        if sum(factorised.values()) > 2:
            print(factorised)


def q66(d):
    return -1


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # assert (timed_function(q66)() == -1)
    assert (timed_function(investigate2)() == 1294299)
