import itertools
from functools import reduce
from operator import mul

from euler.maths.prime import generate_to_sie
from euler.maths.sigma import sigma_n
from euler.util.decorators import timed_function


def q72(number=1000000):
    def pi(numbers):
        # Mathematical notation for multiplying out numbers "sigma of multiplication"
        return reduce(mul, numbers)

    prime_numbers = generate_to_sie(number)
    max_group_size = next(group_size for group_size in range(1, len(prime_numbers))
                          if pi(prime_numbers[:group_size]) > number) - 1
    logging.debug(f'Max group size={max_group_size}, pi={pi(prime_numbers[:max_group_size])}')

    def calculation(factor):
        up_to = (number - 1) // factor
        return sigma_n(up_to)

    calculated = {prime_number: calculation(prime_number) for prime_number in prime_numbers}

    for group_size in range(2, max_group_size + 1):
        logging.debug(f'Group Size={group_size}')
        for group in itertools.combinations(prime_numbers, group_size):
            pass
            # logging.debug(f'Examining::{multiplied}, count={count}')


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q72)() == -1)
