from euler.strings.number_to_string import MILLION
from euler.util.decorators import timed_function


def q85(upper_bound=2 * MILLION):
    def calculate_ways(tuple_):
        w, h = tuple_
        return abs((w * h * (w + 1) * (h + 1)) - upper_bound_4)

    biggest_possible = int(upper_bound ** (1 / 2))  # w * (w+1) * h * (h+1) / 4 < upper_bound
    upper_bound_4 = upper_bound * 4

    # List comprehension of tuples seems to be slower than nested for-loop.
    # I don't think it's worth it to change it back though
    width, height = min([(bigger, smaller) for bigger in range(biggest_possible) for smaller in range(bigger)],
                        key=calculate_ways)
    return width * height


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q85)() == 2772)
