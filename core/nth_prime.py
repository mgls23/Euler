from core.util import prime


# Q7 :: 10001st prime
def q7(n=10001):
    return prime.PrimeGenerator().generate_nth(n)
