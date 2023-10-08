from itertools import combinations

from .euler.maths.prime import is_prime_robin_miller
from .euler.util.decorators import timed_function


def find_primes_with_runs(repeating_number: str, digit: int):
    # All this for a drop of blood - for 5ms difference...
    if primes := primes_with_runs_m_1(repeating_number, digit): return primes

    def helper(repeated_count, different_count):
        if len(string_buffer) == digit:
            generated_number = int(''.join(string_buffer))
            if is_prime_robin_miller(generated_number) and generated_number >= smallest_possible:
                primes.append(generated_number)

            return

        if repeated_count < max_repeat_count:
            string_buffer.append(repeating_number)
            helper(repeated_count + 1, different_count)
            string_buffer.pop()

        if different_count < max_different_count:
            for different in '0123456789':
                if different != repeating_number:
                    string_buffer.append(different)
                    helper(repeated_count, different_count + 1)
                    string_buffer.pop()

    primes = []
    smallest_possible = 10 ** (digit - 1)
    string_buffer = []

    # Because we have a specially optimised case for max_repeat_count = digit - 1
    for max_repeat_count in range(digit - 2, -1, -1):
        max_different_count = digit - max_repeat_count
        helper(0, 0)
        if primes: return primes

    return [-1]


def primes_with_runs_m_1(repeating_number: str, digit: int):
    """ Special case for primes with runs with only 1 difference """
    primes = []
    string_buffer = [repeating_number] * digit
    smallest_possible = 10 ** (digit - 1)

    for different_number in '0123456789':
        if repeating_number == different_number: continue

        for index in range(digit):
            if index: string_buffer[index - 1] = repeating_number

            string_buffer[index] = different_number
            generated_number = int(''.join(string_buffer))

            if is_prime_robin_miller(generated_number) \
                    and generated_number >= smallest_possible:
                primes.append(generated_number)

        string_buffer[-1] = repeating_number

    return primes


def q111():
    return sum(sum(find_primes_with_runs(d, digit=10)) for d in '0123456789')


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q111)() == 612407567715)
