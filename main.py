import argparse

from smallest_multiple import smallest_multiple
from common import prime
from const import problemArgs, ANSWERS


# Q3 :: Largest Prime Factor
def find_primes(n=600851475143):
    """
    Finds prime factors* of a given number
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


# Q6 :: Sum Square Difference
def square_difference(n=100):
    """
    (1 + 2 + 3 + ... n)^2
     = ((n * (n + 1)) / 2) ^ 2

    1^2 + 2^2 + 3^2 + ... n^2
     [BRUTE FORCE]

        Args
        ----
            n: int

        Returns
        -------

    """
    square_of_sum = ((n + 1) * n / 2) ** 2
    sum_of_square = sum([i ** 2 for i in range(n + 1)])
    return square_of_sum - sum_of_square


# Q7 :: 10001st prime
def q_10001th_prime(n=10001):
    return prime.PrimeGenerator().generate_nth(n)


# Q8 :: Adjacent Multiplicand
def adjacent_multiplicand(x, window_size=13):
    """

    Args
    ----
        x
        window_size

    Returns
    -------

    """
    assert x and window_size, "Please provide a number that we could run " \
                              "some cool maths on"

    # Break down x into a list
    x = [int(strx) for strx in (type(x) == int) and str(x) or x]
    y = x[:-1]

    for iteration_count in range(1, window_size):
        for index in range(len(y) - 1):
            y[index] *= x[index + iteration_count]

        y.pop(-1)

    return max(y)


# Q16 :: Digit of 2^1000
def power_digit_sum(power=15):
    """
    1, 2, 4, 8, 16, 32, 64, 128, ...


        Args
        ----
            power

        Returns
        -------
    """
    assert power > 0, "Please provide a number bigger than 0 " \
                      "so we can do some cool maths"

    number_array_repr = [1]
    for i in range(power):

        for j in range(len(number_array_repr)):
            number_array_repr[j] *= 2

        for index in range(len(number_array_repr)):
            while number_array_repr[index] >= 10:
                number_array_repr[index] -= 10
                try:
                    number_array_repr[index + 1] += 1

                except IndexError:
                    number_array_repr.append(1)

    return sum(number_array_repr)


problemHandler = \
    {
        # 1: fizz_buzz,
        3: find_primes,

        5: smallest_multiple,
        6: square_difference,
        7: q_10001th_prime,
        8: adjacent_multiplicand,

        16: power_digit_sum,
    }


def run():
    # Configure Parser + Parse
    parser = argparse.ArgumentParser(description='Project Euler')
    parser.add_argument(
        'n', type=int, help='The Problem Number'
        'p', type=
    )
    args = parser.parse_args()

    # Hack
    index = args.n

    # Execute Problem
    result = problemHandler[index](**problemArgs[index])

    try:
        answer = ANSWERS[index]
        assert (result == answer), \
            'Result for Problem %(index)s is %(result)s ' \
            'and does not match the expect, which is %(answer)s' % locals()

    except KeyError:
        print 'This problem has not been solved yet'
        print 'Output [for problem %(index)s] is %(result)s' % locals()


if __name__ == '__main__':
    run()
