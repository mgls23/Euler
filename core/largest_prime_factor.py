from core.util import prime


# Q3 :: Largest Prime Factor
def q3(n=600851475143):
    """Finds prime factors* of a given number
        * prime factors :: prime numbers that make up the given number
                           once multiplied together

        Args
        ----
            n: int
                the number to conduct the search on primes on

        Returns
        -------
            prime_factors: [int]
                prime numbers that make up the
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
