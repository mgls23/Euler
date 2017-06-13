PRIME_ENTRIES = [2, 3]


def iterator():
    for prime_entry in PRIME_ENTRIES:
        yield prime_entry


def _generate_next_prime():
    candidate = PRIME_ENTRIES[-1] + 2
    while True:
        for prime_number in PRIME_ENTRIES:
            if candidate % prime_number == 0:
                candidate += 2
                break
        else:
            PRIME_ENTRIES.append(candidate)
            return candidate


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
    while PRIME_ENTRIES[-1] < number:
        _generate_next_prime()

    return PRIME_ENTRIES


def nth_prime_number(n):
    primes_to_generate = n - len(PRIME_ENTRIES)
    for _ in range(primes_to_generate + 1):
        _generate_next_prime()

    return PRIME_ENTRIES[n - 1]
