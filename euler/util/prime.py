import math

PRIME_ENTRIES = [2, 3, 5, 7]


def iterator():
    for prime_entry in PRIME_ENTRIES:
        yield prime_entry


def _check_prime_entries(number):
    for prime_number in PRIME_ENTRIES:
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


def is_prime(number):
    if number <= 1: return False
    if number <= 3: return True
    if (number % 2 == 0) or (number % 3 == 0): return False

    for i in range(5, math.floor(math.sqrt(number)) + 1, 6):
        if (number % i) == 0 or (number % (i + 2)) == 0:
            return False

    return True
