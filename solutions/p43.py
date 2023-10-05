import logging
import sys
from math import ceil

from euler.util.decorators import timed_function


def is_partially_pandigital(number_string):
    return len(set(number_string)) == len(number_string)


def guess_first_two_digit(possibilities, divisible_by):
    confirmed = []
    for digits in possibilities:
        first_digit = str(digits)[:1]
        for prefix_2_digits in map(str, range(1, 100)):
            if int(prefix_2_digits + first_digit) % divisible_by == 0:
                new_entry = prefix_2_digits.zfill(2) + str(digits)
                if is_partially_pandigital(new_entry):
                    confirmed.append(new_entry)

    return confirmed


def guess_first_digit(possibilities, divisible_by):
    confirmed = []
    for digits in possibilities:
        first_two_digits = str(digits)[:2]
        for prefix_digit in map(str, range(10)):
            if int(prefix_digit + first_two_digits) % divisible_by == 0:
                new_entry = prefix_digit.zfill(1) + str(digits)
                if is_partially_pandigital(new_entry):
                    confirmed.append(new_entry)

    return confirmed


def guess_last_digit(possibilities, divisible_by):
    confirmed = []
    for digits in possibilities:
        last_two_digits = str(digits)[-2:]
        for suffix_digit in map(str, range(10)):
            if int(last_two_digits + suffix_digit) % divisible_by == 0:
                new_entry = str(digits) + suffix_digit
                if is_partially_pandigital(new_entry):
                    confirmed.append(new_entry)

    return confirmed


def any_first_two_that_fits(possibilities):
    confirmed = []
    all_digits = set(map(str, range(10)))
    for digits in possibilities:
        difference = list(all_digits - set(digits))
        confirmed.append(int(''.join(difference) + digits))
        confirmed.append(int(''.join(difference[::-1]) + digits))

    return sorted(confirmed)


def q43():
    # 5, 11
    d6_to_d8 = list(map(str, range(ceil(500 / 11) * 11, 600, 11)))  # d6 = 5, d678 = 5XX and multiple of 11
    logging.debug(f'd6_to_d8 = {d6_to_d8}')

    # 13
    d6_to_d9 = guess_last_digit(d6_to_d8, 13)
    logging.debug(f'd6_to_d9 = {d6_to_d9}')

    # 17
    d6_to_d10 = guess_last_digit(d6_to_d9, 17)
    logging.debug(f'd6_to_d10={d6_to_d10}')

    # 7
    d5_to_d10 = guess_first_digit(d6_to_d10, 7)
    logging.debug(f'd5_to_d10={d5_to_d10}')

    # 3
    d3_to_d10 = guess_first_two_digit(d5_to_d10, 3)
    logging.debug(f'd3_to_d10={d3_to_d10}')

    # 2
    d3_to_d10_with_2 = list(filter(lambda number: int(str(number)[1]) % 2 == 0, d3_to_d10))
    logging.debug(f'd3_to_d10_with_2={d3_to_d10_with_2}')

    pandigital_numbers = any_first_two_that_fits(d3_to_d10_with_2)
    logging.debug(f'Pandigital Numbers = {pandigital_numbers}')

    return sum(pandigital_numbers)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q43)() == 16695334890)
