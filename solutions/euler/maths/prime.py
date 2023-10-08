import collections
import math
import random

from euler.util.decorators import memoised, timed_function


class PrimeGenerator:
    def __init__(self):
        self.prime_numbers = [2, 3, 5, 7]

    def _check_prime_entries(self, number):
        square_root = math.sqrt(number)
        for prime_number in self.prime_numbers:
            if prime_number > square_root: break
            if number % prime_number == 0:
                return False

        self.prime_numbers.append(number)
        return True

    def _generate_next_prime(self):
        starting_length = len(self.prime_numbers)
        i = math.ceil((self.prime_numbers[-1] - 1) / 6)

        while starting_length == len(self.prime_numbers):
            i += 1
            k = i * 6
            self._check_prime_entries(k - 1)
            self._check_prime_entries(k + 1)

        return self.prime_numbers[-1]

    def nth_prime_number(self, n):
        while len(self.prime_numbers) < n:
            self._generate_next_prime()

        return self.prime_numbers[n - 1]

    def prime_numbers_smaller_than(self, number):
        while self._generate_next_prime() < number:
            pass

        return self.prime_numbers


def generate_primes_in_range(lower_limit, upper_limit):
    return filter(lambda n: n >= lower_limit, generate_to_sie(upper_limit))


def generate_primes_in_digit_range(lower_limit_digit, upper_limit_digit):
    return generate_primes_in_range(10 ** lower_limit_digit, 10 ** upper_limit_digit)


def generate_to_sie(upper_bound):
    """ Prime numbers generation using Sieve of Eratosthenes [https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes]"""
    prime_numbers = []
    considered = [True] * upper_bound

    for number in range(2, upper_bound):
        if considered[number]:
            prime_numbers.append(number)
            considered[number * 2::number] = [False] * (((upper_bound - 1) // number) - 1)

    return prime_numbers


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

        if x in [1, n - 1]: continue  # Probably prime

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

    return all(
        (number % i) == 0 or (number % (i + 2)) == 0
        for i in range(5, math.ceil(math.sqrt(number)) + 1, 6)
    )


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
    if primes is None: primes = generate_to_sie(number)

    prime_composition = collections.defaultdict(int)
    for prime_number in primes:
        while number % prime_number == 0:
            prime_composition[prime_number] += 1
            number //= prime_number
            if number == 1: return prime_composition

    assert is_prime(number) or number == 1, f"Not Enough Primes provided - number={number}, primes={primes}"
    prime_composition[number] = 1
    return prime_composition
