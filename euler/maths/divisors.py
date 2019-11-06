import operator
from functools import reduce

from euler.maths.multiplications import decompose_to_prime_powers


def sum_of_divisors(n, primes):
    return reduce(operator.mul,
                  [_sum_of_divisors(prime_number, power)
                   for prime_number, power in decompose_to_prime_powers(n, primes).items()])


def _sum_of_divisors(prime_number, power):
    return (prime_number ** (power + 1) - 1) // (prime_number - 1)


def sum_of_proper_divisors(n, primes):
    return sum_of_divisors(n, primes) - n


def factorise_by(number, prime_number):
    """ Returns 1 iteration of decompose to prime powers - where it shows how many times
    the prime number factors into this number

    :param number: int
    :param prime_number: int
    :return: remaining_number, power
    """
    power = 0
    while number % prime_number == 0:
        number //= prime_number
        power += 1

    return number, power
