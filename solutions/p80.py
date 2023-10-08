from decimal import Decimal, getcontext

from .euler.util.decorators import timed_function


def square_root_2(iteration_count=200):
    x = 1
    for _ in range(iteration_count):
        x = 1 / (2 + x)

    return 1 + x


def square_root_n(number, iteration_count=10000):
    # noinspection SpellCheckingInspection
    getcontext().prec = 100 + 100

    n_minus_1 = number - 1
    x = Decimal(n_minus_1)

    for _ in range(iteration_count):
        x = n_minus_1 / (2 + x)

    return 1 + x


def get_sum_of_hundred_decimal_digits(number):
    square_root = square_root_n(number)
    return sum(map(int, str(square_root).replace('.', '')[:100]))


def q80():
    return sum(get_sum_of_hundred_decimal_digits(number) for number in range(2, 100))


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(get_sum_of_hundred_decimal_digits)(2) == 475)
    assert (timed_function(q80)() == 40930)
