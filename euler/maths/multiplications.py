import collections
import functools
import math
import operator


def lowest_common_multiple(number1, number2):
    return number1 * number2 / greatest_common_denominator(number1, number2)


def greatest_common_denominator(number1, number2):
    bigger, smaller = max(number1, number2), min(number1, number2)
    mod = bigger % smaller
    while mod > 1:
        bigger, smaller = smaller, mod
        mod = bigger % smaller

    return mod == 0 and smaller or mod


def merge_prime_powers(*prime_powers):
    merged_prime_powers = collections.defaultdict(int)
    for prime_power in prime_powers:
        for prime, power in prime_power.items():
            merged_prime_powers[prime] += power

    return merged_prime_powers


def multiply_out_numbers_in_powers(number_in_powers):
    """ Finds the multiplicative sum [pi] of factors with its powers (should be prime powers)

    :param number_in_powers: dict
    :returns: (key ^ value) * (key ^ value) ...
    """
    return math.prod([number ** power for number, power in number_in_powers.items()])
