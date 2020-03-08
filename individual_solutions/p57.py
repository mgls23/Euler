from functools import reduce

from euler.util.decorators import timed_function


def square_root_2_generator(stop_iteration):
    numerator, denominator = 1, 1
    for _ in range(stop_iteration):
        numerator += denominator * 2
        denominator = numerator - denominator

        yield numerator, denominator


def numerator_has_more_digits(numerator, denominator):
    return len(str(numerator)) > len(str(denominator))


def q57(number=1000):
    return reduce(lambda count, fraction: numerator_has_more_digits(*fraction) and count + 1 or count,
                  square_root_2_generator(number), 0)


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q57)() == 153)
