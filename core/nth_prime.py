from core.util import prime


def find_nth_prime(n):
    return prime.PrimeGenerator().generate_nth(n)


# Q7 :: 10001st prime
def q7():
    return find_nth_prime(10001)
