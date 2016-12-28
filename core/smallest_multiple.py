from core.util.prime import PrimeGenerator


def cumulative_lcm_in_prime_powers(n):
    """ Given a number, finds the
    :param n: int
    :returns: dict
    """
    if n <= 1: return {}

    max_prime_factors = {}
    primes = PrimeGenerator().generate_to(n)

    for number in range(primes[0], n):
        prime_powers = decompose_to_prime_powers(number, primes)

        for prime, power in prime_powers.iteritems():
            max_prime_factors[prime] = \
                max(max_prime_factors.get(prime, 0), power)

    return max_prime_factors


def decompose_to_prime_powers(number, primes):
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
    prime_composition = {}
    for prime_number in primes:
        while not number % prime_number:
            if prime_composition.has_key(prime_number):
                prime_composition[prime_number] += 1

            else:
                prime_composition[prime_number] = 1

            number /= prime_number
            if number == 1:
                assert number == multiply_out_numbers_in_powers(
                    prime_composition)
                return prime_composition

    assert False, "Bad Programmer Error"


def multiply_out_numbers_in_powers(number_in_powers):
    """ Finds the multiplicative sum [pi] of factors with indicated powers

    Args
    ----
        number_in_powers:
            {
                N1: a,
                N2: b,
                N3: c,
                ...
            }
    Returns
    -------
        (N1 ^ a) * (N2 ^ b) * (N3 ^ c) * ...
    """
    return reduce(
        lambda x, y: x * y,
        [
            number ** power
            for number, power in number_in_powers.iteritems()
        ]
    )


def q5(n=20):
    cumulative_lcm = cumulative_lcm_in_prime_powers(n)
    smallest_multiple_up_to_n = multiply_out_numbers_in_powers(
        cumulative_lcm
    )
    return smallest_multiple_up_to_n


if __name__ == '__main__':
    print q5()
