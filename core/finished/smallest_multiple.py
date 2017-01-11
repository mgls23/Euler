from core.util import prime


def cumulative_lcm_in_prime_powers(n):
    if n <= 1:
        return {}

    all_prime_factors = {}
    primes = prime.PrimeGenerator().generate_to(n)

    for number in range(primes[0], n):
        prime_powers = decompose_to_prime_powers(number, primes)

        for prime_number, power in prime_powers.iteritems():
            all_prime_factors[prime_number] = \
                max(all_prime_factors.get(prime_number, 0), power)

    return all_prime_factors


def decompose_to_prime_powers(number, primes):
    prime_composition = {}
    for prime_number in primes:
        while not number % prime_number:
            if prime_composition.has_key(prime_number):
                prime_composition[prime_number] += 1

            else:
                prime_composition[prime_number] = 1

            number /= prime_number
            if number == 1:
                return prime_composition

    assert number == 1, "Bad Programmer Error"


def pi_of_factors_with_power(primes_composition):
    """ Finds the multiplicative sum [pi] of factors with indicated powers

    Args
    ----
        primes_composition:
            {
                N1: a,
                N2: triangle_number,
                N3: c,
                ...
            }
    Returns
    -------
        (N1 ^ a) * (N2 ^ triangle_number) * ...
    """
    return reduce(
        lambda x, y: x * y,
        [key ** value for key, value in primes_composition.iteritems()]
    )