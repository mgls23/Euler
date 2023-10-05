import math

from euler.strings.number_to_string import SPECIAL_MODULO, BILLION
from euler.util.decorators import timed_function
from solutions.p72 import geometric_sum


def inverse_digit_sum(number):
    number_of_nines, leading_number = number // 9, number % 9
    return int(str(leading_number) + number_of_nines * '9') % SPECIAL_MODULO


def big_s_brute_force(number):
    return sum([inverse_digit_sum(i) for i in range(1, number + 1)])


def big_s_efficient(number):
    number_of_nines, leading_number = number // 9, number % 9

    first_part = geometric_sum(45, ratio=10, number=number_of_nines)
    first_part += leading_number * (leading_number + 1) // 2 * 10 ** number_of_nines

    second_part = 81 * b(number_of_nines - 1) + int(('9' * number_of_nines) or '0') * leading_number
    return int(first_part + second_part)


def a():
    start = 0
    for i in range(19, 30):
        addition = int('1' * i)
        start += addition
        print(i, addition, start)


def b(number):
    prefix = '12345678'[:(number - 1) % 9]
    suffix = str(((number - 1) % 9) + 1) * (((number - 1) // 9 * 9) + 1)

    incomplete = int(prefix + suffix) % SPECIAL_MODULO
    useful = int(math.ceil(number / 9)) - 2

    for i in range(useful + 1):
        incomplete += (123456789 * (BILLION ** i)) % SPECIAL_MODULO
        incomplete += int('9' * (i * 9) or '0') % SPECIAL_MODULO

    return incomplete % SPECIAL_MODULO


def b_brute_force(number):
    start = 0
    for i in range(1, number + 1):
        start += int('1' * i)

    return start


def verify_b():
    for i in range(1, 50):
        b1, b2 = b(i), b_brute_force(i)
        assert b1 == b2, f'{i, b1, b2}'


def q684(lower_bound=2, upper_bound=90):
    sum_ = 0

    fibonacci_sequence = [0, 1]
    for i in range(lower_bound, upper_bound + 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 2] + fibonacci_sequence[i - 1])
        sum_ += big_s_efficient(inverse_digit_sum(fibonacci_sequence[i]))

    return sum_ % SPECIAL_MODULO


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # assert (timed_function(big_s_brute_force)(20) == 1074)
    # assert (timed_function(big_s_efficient)(20) == 1074)
    #
    assert (timed_function(q684)(1, 12) == 1074)
    # verify_b()
    # a()
