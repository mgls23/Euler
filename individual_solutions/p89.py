import logging

from euler.util.decorators import timed_function
from euler.util.io import datafiles


def test_roman_numerals():
    assert roman_numerals(1) == 1


def roman_numerals_optimal(number: int) -> int:
    assert number < 5000

    def single_digit(digit: str) -> int:
        return {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 2,
            '5': 1,
            '6': 2,
            '7': 3,
            '8': 4,
            '9': 2,
        }[digit]

    sum_of_digits = sum(map(single_digit, str(number)))
    if number >= 4000: sum_of_digits += 2  # when the number is 4XXXX, it cannot be simplified
    return sum_of_digits


def roman_numerals(number: str) -> int:
    def convert(character: str) -> int:
        return {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }[character]

    total = 0
    converted = list(map(convert, number))
    for i, value in enumerate(converted):
        if i < len(converted) - 1 and converted[i + 1] > value:
            total -= value
        else:
            total += value

    return total


def read_roman_numerals():
    with open(datafiles('p089_roman.txt')) as file:
        raw_input = file.readlines()
        return [word.replace('\n', '') for word in raw_input]


def q89() -> int:
    saved = 0
    for roman_numeral in read_roman_numerals():
        raw_value = roman_numerals(roman_numeral)
        should_be = roman_numerals_optimal(raw_value)
        assert should_be <= len(roman_numeral)
        saved += len(roman_numeral) - should_be

    return saved


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    assert (timed_function(q89)() == 743)
