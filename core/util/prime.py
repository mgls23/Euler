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


def prime_numbers_smaller_than(number):
    while PRIME_ENTRIES[-1] < number:
        _generate_next_prime()

    return PRIME_ENTRIES


def nth_prime_number(n):
    primes_to_generate = n - len(PRIME_ENTRIES)
    for _ in range(primes_to_generate + 1):
        _generate_next_prime()

    return PRIME_ENTRIES[n - 1]
