from euler.util.decorators import timed_function
from euler.strings.english import convert_to_english


def function(power, last_digit_index):
    number = pow(2, power)
    try:
        return str(number)[-1 * last_digit_index]
    except IndexError:
        return '-'


def has_pattern(digits):
    starts_at = 0
    while digits[0] == '-':
        starts_at += 1
        digits.pop(0)

    for assumed_length in range(2, len(digits) // 2 + 1):
        if digits[:assumed_length] == digits[assumed_length:assumed_length * 2]:
            return starts_at, assumed_length, digits[:assumed_length]

    return starts_at, -1, []


def investigate():
    for digit_index in range(1, 10):
        digits = [function(power, digit_index) for power in range(1, 10000)]
        print(f'{convert_to_english(digit_index)} Digits={digits}')
        print(has_pattern(digits))


def q97():
    return -1


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # assert (timed_function(q97)() == -1)
    investigate()
