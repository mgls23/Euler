from euler.util import prime


def largest_prime_factor(number):
    """ Finds a set of prime numbers [prime factors] returns the original
    number once multiplied together

    :param number: int (The number to conduct the search on primes on)
    """
    prime_factors = []
    m = number

    for index, prime_number in enumerate(prime.iterator(), 1):
        if m % prime_number == 0:
            m /= prime_number
            prime_factors.append(prime_number)

        if m <= 1 or prime_number > number:
            break

        if index >= len(prime.PRIME_ENTRIES):
            prime._generate_next_prime()

    return max(prime_factors)
