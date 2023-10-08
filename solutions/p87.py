from solutions.euler.maths.prime import generate_to_sie
from solutions.euler.strings.number_to_string import MILLION
from solutions.euler.util.decorators import timed_function


def q87(upper_bound=50 * MILLION):
    possible_primes = generate_to_sie(int((upper_bound - 2 ** 3 - 2 ** 4) ** 0.5))
    prime_power_triple = list()

    for fourth_power in possible_primes:
        after_fourth = upper_bound - fourth_power ** 4
        for cube in possible_primes:
            after_cube = after_fourth - cube ** 3
            if after_cube < 0: break  # no need to check for larger

            for square in possible_primes:
                after_square = after_cube - square ** 2
                if after_square < 0: break  # no need to check for larger
                prime_power_triple.append(upper_bound - after_square)
                # logging.debug(f'{square, cube, fourth_power, prime_power_triple[-1]}')

    return len(set(prime_power_triple))


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q87)() == -1)
