import math

from sympy import totient

from euler.maths.prime import generate_to_sie
from euler.util.decorators import timed_function


def q72(number=1000000):
    prime_numbers = generate_to_sie(number)
    visited = [False] * number

    next_prime_number = prime_numbers.pop(0)
    summed = 0
    for i in range(2, number):
        if i == next_prime_number:
            last_power = int(math.log(number, i))
            progression_sum = geometric_sum(start=1, ratio=i, number=last_power)
            for j in range(2, last_power + 1):
                visited[i ** j] = True

            summed += progression_sum
        elif not visited[i]:
            summed += totient(i)

    return summed


def brute_force(number):
    # for i in range(2, number): logging.debug(i, totient(i))
    return sum(map(totient, range(2, number)))


def geometric_sum(start: int, ratio: int, number: int):
    return start * (ratio ** number - 1) / (ratio - 1)


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # assert (timed_function(geometric_sum)(3, 3, 2) == 12)
    # assert (timed_function(geometric_sum)(2, 7, 3) == 114)

    assert (timed_function(q72)(1000) == brute_force(1000))
    assert (timed_function(q72)() == -1)
