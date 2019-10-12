from euler.util.multiplications import decompose_to_prime_powers, multiply_out_numbers_in_powers
from euler.util.prime import prime_numbers_smaller_than


def cumulative_lcm_in_prime_powers(n):
    """ Given a number, finds the lowest common multiplicand
    :param n: int
    :returns: dict
    """
    if n <= 1:
        return {}

    max_prime_factors = {}
    primes = prime_numbers_smaller_than(n)

    for number in range(primes[0], n):
        prime_powers = decompose_to_prime_powers(number, primes)

        for prime, power in prime_powers.items():
            max_prime_factors[prime] = \
                max(max_prime_factors.get(prime, 0), power)

    return max_prime_factors


def smallest_multiple_up_to(n):
    return multiply_out_numbers_in_powers(cumulative_lcm_in_prime_powers(n))
