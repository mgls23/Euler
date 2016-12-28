from core.util import prime


def largest_prime_factor(n):
    """ Finds a set of prime numbers [prime factors] returns the original
    number once multiplied together

    Args
    ----
        :param n: int
            the number to conduct the search on primes on
    """
    prime_factors = []
    prime_iterator = prime.PrimeGenerator()
    prime_number = 1
    x_copy = n

    while x_copy > 1 and prime_number < n:
        prime_number = prime_iterator.next()
        if x_copy % prime_number == 0:
            x_copy /= prime_number
            prime_factors.append(prime_number)

    return max(prime_factors)


# Q3 :: Largest Prime Factor of 600851475143
def q3():
    return largest_prime_factor(600851475143)
