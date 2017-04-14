import functools

from euler.util import prime


def cumulative_lcm_in_prime_powers(n):
    """ Given a number, finds the lowest common multiplicand
    :param n: int
    :returns: dict
    """
    if n <= 1:
        return {}

    max_prime_factors = {}
    primes = prime.generate_to(n)

    for number in range(primes[0], n):
        prime_powers = decompose_to_prime_powers(number, primes)

        for prime, power in prime_powers.items():
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
            if prime_number in prime_composition:
                prime_composition[prime_number] += 1

            else:
                prime_composition[prime_number] = 1

            number /= prime_number
            if number == 1:
                return prime_composition

    assert False, "Bad Programmer Error"


def multiply_out_numbers_in_powers(number_in_powers):
    """ Finds the multiplicative sum [pi] of factors with indicated powers
    
    :param number_in_powers: dict
    :returns: (key ^ value) * (key ^ value) ...
    """
    powers = [number ** power for number, power in number_in_powers.items()]
    return functools.reduce(lambda x, y: x * y, powers)


def smallest_multiple_up_to(n):
    return multiply_out_numbers_in_powers(cumulative_lcm_in_prime_powers(n))


def q5():
    return smallest_multiple_up_to(20)


if __name__ == '__main__':
    print(q5())
