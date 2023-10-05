import math

from euler.sequence.polygonal import Pentagonal
from euler.util.decorators import timed_function


def q44():
    pentagonal = Pentagonal()
    pentagonal_numbers = [0, 1]

    for bigger in range(2, 2500):  # arbitrary upper_limit
        pentagonal_numbers.append(pentagonal.to_number(bigger))
        for smaller in range(1, bigger):
            if pentagonal.is_pentagonal(pentagonal_numbers[bigger] + pentagonal_numbers[smaller]) and \
                    pentagonal.is_pentagonal(pentagonal_numbers[bigger] - pentagonal_numbers[smaller]):
                return pentagonal_numbers[bigger] - pentagonal_numbers[smaller]


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q44)() == 5482660)
