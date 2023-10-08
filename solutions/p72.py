from sympy import totient

from solutions.euler.util.decorators import timed_function


def q72(number=1000000):
    visited = list(range(number + 1))
    summed = 0

    for index in range(2, number + 1):  # don't use enumerate/iterator
        # Prime Number
        if index == visited[index]:
            summed += index - 1

            # reverse - sieve: decrease by (p-1)/p
            for to_update in range(index * 2, number + 1, index):
                visited[to_update] *= (index - 1) / index

        # Composite / power - already decreased
        else:
            summed += visited[index]

    return int(summed)


def brute_force(number):
    # for i in range(2, number): logging.debug(i, totient(i))
    return sum(map(totient, range(2, number + 1)))


def geometric_sum(start: int, ratio: int, number: int):
    return start * ((ratio ** number) - 1) // (ratio - 1)


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # assert (timed_function(geometric_sum)(3, 3, 2) == 12)
    # assert (timed_function(geometric_sum)(2, 7, 3) == 114)

    # assert (timed_function(q72)(8) == 21)
    # assert (timed_function(q72)(100) == brute_force(100))
    assert (timed_function(q72)() == 303963552391)
