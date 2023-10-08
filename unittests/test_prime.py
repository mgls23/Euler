import unittest

from solutions.euler.maths.prime import is_prime_robin_miller


class TestRobinMillerPrime(unittest.TestCase):
    def test_basic(self):
        primes = [2, 3, 5, 7, ]
        for prime_number in primes:
            self.assertEqual(is_prime_robin_miller(prime_number), True, prime_number)
