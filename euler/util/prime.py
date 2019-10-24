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


COMPUTED = {}


def is_prime_memoised(number):
    if number in COMPUTED: return COMPUTED[number]

    primality = is_prime(number)
    COMPUTED[number] = primality
    return primality


def is_truncable_prime(number, digit_length=-1):
    if not is_prime_memoised(number): return False
    if digit_length == -1: digit_length = int(math.floor(math.log10(number)) + 1)

    for dividing_point in range(1, digit_length):
        div = number // 10 ** dividing_point
        mod = number % 10 ** dividing_point

        if not (is_prime_memoised(div) and is_prime_memoised(mod)):
            return False

    return True
