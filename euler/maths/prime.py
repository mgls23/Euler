import math
import random

from euler.util.decorators import memoised, timed_function

PRIME_ENTRIES = [2, 3, 5, 7]


def iterator():
    for prime_entry in PRIME_ENTRIES:
        yield prime_entry


def _check_prime_entries(number):
    square_root = math.sqrt(number)
    for prime_number in PRIME_ENTRIES:
        if prime_number > square_root: break
        if number % prime_number == 0:
            return False

    PRIME_ENTRIES.append(number)
    return True


def _generate_next_prime():
    starting_length = len(PRIME_ENTRIES)
    i = math.ceil((PRIME_ENTRIES[-1] - 1) / 6)

    while starting_length == len(PRIME_ENTRIES):
        i += 1
        k = i * 6
        _check_prime_entries(k - 1)
        _check_prime_entries(k + 1)

    return PRIME_ENTRIES[-1]


def generate_primes_in_range(lower_limit, upper_limit):
    return filter(lambda n: n >= lower_limit, generate_to_sie(upper_limit))


def generate_primes_in_digit_range(lower_limit_digit, upper_limit_digit):
    return generate_primes_in_range(10 ** lower_limit_digit, 10 ** upper_limit_digit)


def generate_to_sie(upper_bound):
    """ Prime numbers generation using Sieve of Eratosthenes
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    global PRIME_ENTRIES
    PRIME_ENTRIES = []

    considered = [True] * upper_bound

    for number in range(2, upper_bound):
        if considered[number]:
            PRIME_ENTRIES.append(number)

            considered[number * 2::number] = \
                [False] * (((upper_bound - 1) // number) - 1)

    return PRIME_ENTRIES


def prime_numbers_smaller_than(number):
    while _generate_next_prime() < number:
        pass

    return PRIME_ENTRIES


def nth_prime_number(n):
    while len(PRIME_ENTRIES) < n:
        _generate_next_prime()

    return PRIME_ENTRIES[n - 1]


def is_prime_robin_miller(n, k=2):
    if n <= 1: return False
    if n <= 3: return True
    if (n % 2 == 0) or (n % 3 == 0): return False

    # n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1: continue  # Probably prime

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == (n - 1): break  # Probably prime

        else:
            return False

    return True


@memoised
def is_prime(number):
    if number <= 1: return False
    if number <= 3: return True
    if (number % 2 == 0) or (number % 3 == 0): return False

    for i in range(5, math.floor(math.sqrt(number)) + 1, 6):
        if (number % i) == 0 or (number % (i + 2)) == 0:
            return False

    return True


def is_truncable_prime(number, digit_length=-1):
    if not is_prime(number): return False
    if digit_length == -1: digit_length = int(math.floor(math.log10(number)) + 1)

    for dividing_point in range(1, digit_length):
        div = number // 10 ** dividing_point
        mod = number % 10 ** dividing_point

        if not (is_prime(div) and is_prime(mod)):
            return False

    return True


@timed_function
def _benchmark_for_generate_sie(lower_range_digit=6, upper_range_digit=7):
    return generate_primes_in_digit_range(lower_range_digit, upper_range_digit)


@timed_function
def _benchmark_generate_by_robin_miller(lower_range_digit=5, upper_range_digit=6):
    return [number for number in range(10 ** lower_range_digit, 10 ** upper_range_digit) if
            is_prime_robin_miller(number)]


if __name__ == '__main__':
    import logging, sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    _benchmark_for_generate_sie(lower_range_digit=6, upper_range_digit=7)
    _benchmark_generate_by_robin_miller(lower_range_digit=5, upper_range_digit=6)
