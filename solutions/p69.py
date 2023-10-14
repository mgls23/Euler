from functools import reduce
from math import sqrt, ceil
from operator import mul

from solutions.euler.maths.prime import generate_to_sie
from solutions.euler.maths.ungrouped import phi
from solutions.euler.util.decorators import timed_function


def q69(upper_limit=10 ** 6):
    prime_numbers = generate_to_sie(ceil(sqrt(upper_limit)))
    highly_divisible_number = reduce(mul, generate_to_sie(17 + 1))

    maximum_ratio = 1
    number_at_maximum = 1

    for number in range(highly_divisible_number, upper_limit, highly_divisible_number):
        ratio = number / phi(number, prime_numbers)
        if ratio > maximum_ratio:
            maximum_ratio = ratio
            number_at_maximum = number

    return number_at_maximum


if __name__ == '__main__':
    assert (timed_function(q69)() == 510510)
