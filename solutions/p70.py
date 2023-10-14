import itertools
from collections import Counter
from fractions import Fraction
from math import sqrt, ceil

from solutions.euler.maths.prime import generate_to_sie
from solutions.euler.maths.ungrouped import _phi
from solutions.euler.util.decorators import timed_function


# Not tested - need to be profiled
def ranged_phi(upper_limit):
    prime_numbers = generate_to_sie(upper_limit)

    calculated_phis = list(range(upper_limit + 1))
    for prime_number in prime_numbers:
        calculated_phis[prime_number] = prime_number - 1
        calculated_phis[prime_number * 2::prime_number] = list(
            map(lambda number: number * 1 - Fraction(1, prime_number),
                calculated_phis[prime_number * 2::prime_number]))

    return [int(calculated) for calculated in calculated_phis]


def q70(given_number=10 ** 7):
    range_multiplier = 1.5

    primes = generate_to_sie(ceil(sqrt(given_number) * range_multiplier))
    primes_in_range = [prime for prime in primes if ceil(sqrt(given_number) / range_multiplier) < prime]

    minimum_ratio = 2
    number_at_minimum = given_number

    for prime1, prime2 in itertools.combinations(primes_in_range, 2):
        number = prime1 * prime2
        if number > given_number: continue

        result = _phi(number, prime1, prime2)
        if Counter(str(result)) == Counter(str(number)):
            ratio = number / result
            if ratio < minimum_ratio:
                number_at_minimum = number
                minimum_ratio = ratio

    return number_at_minimum


if __name__ == '__main__':
    assert (timed_function(q70)() == 8319823)
