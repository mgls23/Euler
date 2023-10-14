import math

from solutions.euler.strings.number_to_string import MILLION, TEN
from solutions.euler.util.decorators import timed_function

INPUT = TEN * MILLION


def q92(upper_bound=INPUT):
    _, chain_89 = memoised_chain(upper_bound)
    return len(chain_89)


def memoised_chain(upper_bound):
    chain_1, chain_89 = {1}, {89}

    for number in range(2, upper_bound):
        trail = {number}

        while True:
            if number in chain_1:
                chain_1 |= trail
                break

            if number in chain_89:
                chain_89 |= trail
                break

            number = sum(map(lambda x: x ** 2, map(int, str(number))))
            trail.add(number)

    return chain_1, chain_89


def semi_optimal(upper_bound=INPUT):
    """ @anonymous [https://projecteuler.net/thread=92;page=2]
    Uses the fact that the numbers after 1 iteration cannot exceed (9 ** 2) * int(math.ceil(math.log(number, 10))) + 1
    """

    to_1, to_89 = 0, 1

    def pre_compute(number):
        semi_upper_bound = (9 ** 2) * int(math.ceil(math.log(number, 10))) + 1
        chain_1, chain_89 = memoised_chain(semi_upper_bound)

        precomputed = [-1] * (semi_upper_bound + 1)
        for element in chain_89: precomputed[element] = to_89

        return precomputed, semi_upper_bound

    all_range, largest = pre_compute(upper_bound)
    sum_ = all_range.count(to_89)
    for i in range(largest, upper_bound + 1):
        if all_range[sum(map(lambda x: x ** 2, map(int, str(i))))]:
            sum_ += 1

    return sum_


def most_optimal_answer():
    """ @jackdied [https://projecteuler.net/thread=92] """

    def one_or_89(number):
        while number != 89 and number != 1:
            number = sum(map(lambda x: x * x, map(int, str(number))))

        return number

    def main():
        last = {0: 1}
        squares = [(x * x) for (x) in range(10)]  # [0, 1, 4 .. 81]
        for _ in range(7):  # number of digits
            next_ = {}
            for (total, result) in last.items():
                for square in squares:
                    number_total = total + square
                    try:
                        next_[number_total] += result
                    except KeyError:
                        next_[number_total] = result
            print(next_)
            last = next_

        result = {1: 0, 89: 0}
        del last[0]  # causes one_or_89 to infinite loop

        for (k, square) in last.items():
            result[one_or_89(k)] += square

        return result[89]

    return main()


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # assert (timed_function(q92)() == 8581146)
    # assert (timed_function(most_optimal_answer)() == 8581146)
    assert (timed_function(semi_optimal)() == 8581146)
