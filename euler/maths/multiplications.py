import collections
import functools
import math

from euler.maths.prime import prime_numbers_smaller_than


def lowest_common_multiple(number1, number2):
    return number1 * number2 / greatest_common_denominator(number1, number2)


def greatest_common_denominator(number1, number2):
    bigger, smaller = max(number1, number2), min(number1, number2)
    mod = bigger % smaller
    while mod > 1:
        bigger, smaller = smaller, mod
        mod = bigger % smaller

    return mod == 0 and smaller or mod


def multiply(*prime_powers):
    multiplied = collections.defaultdict(int)
    for prime_power in prime_powers:
        for prime, power in prime_power.items():
            multiplied[prime] += power

    return multiplied


def decompose_to_prime_powers(number, primes=None):
    """ Decomposes a given number into a set of prime number paired with
    powers which multiplied out, gives the original number

        Args
        ----
            :param number: int
                The given number to decompose

            :param primes: list
                Prime numbers that does not exceed the number

        Returns
        -------
            {
                N1: P1,
                N2: P2,
                N3: P3,
                ...
                Nm, Pm,
            } ... (N1 ^ P1) * (N2 ^ P2) * ... = number
    """
    assert number > 0
    if number == 1: return {}
    if primes is None: primes = prime_numbers_smaller_than(int(math.ceil(math.sqrt(number))))

    prime_composition = collections.defaultdict(int)
    for prime_number in primes:
        while number % prime_number == 0:
            prime_composition[prime_number] += 1
            number //= prime_number
            if number == 1: return prime_composition

    assert False, f"Not Enough Primes provided - number={number}, primes={primes}"


def multiply_out_numbers_in_powers(number_in_powers):
    """ Finds the multiplicative sum [pi] of factors with indicated powers

    :param number_in_powers: dict
    :returns: (key ^ value) * (key ^ value) ...
    """
    powers = [number ** power for number, power in number_in_powers.items()]
    return functools.reduce(lambda x, y: x * y, powers)
