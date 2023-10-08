from solutions.euler.maths import prime
from solutions.euler.maths.multiplications import lowest_common_multiple
from solutions.euler.maths.sigma import sigma_n, sigma_n2

from solutions.p62 import q62


def q5(up_to=20):
    if up_to <= 1: return up_to

    cumulative = 2
    for number in range(3, up_to + 1):
        cumulative = lowest_common_multiple(cumulative, number)

    return int(cumulative)


def q6(n=100):
    # Q6 :: Sum Square Difference
    square_of_sum = sigma_n(n) ** 2
    sum_of_square = sigma_n2(n)
    return square_of_sum - sum_of_square


def q7():
    return prime.PrimeGenerator().nth_prime_number(10001)


def q28():
    """ Q28 :: Number spiral diagonals [https://projecteuler.net/problem=28]

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
    """
    side_length = 1001
    one_side = (side_length - 1) // 2

    return int(((16 * (one_side ** 3) + 30 * (one_side ** 2) + 26 * one_side) / 3) + 1)


def q71(number=1000000):
    numerator, denominator = 3, 7

    expanded_fraction_denominator = (number // denominator) * denominator
    expanded_fraction_numerator = (expanded_fraction_denominator * numerator) // denominator

    return expanded_fraction_numerator - 1  # Because n-1 and n are co-primes


SIMPLIFIED = [q5, q6, q7, q28, q62]
