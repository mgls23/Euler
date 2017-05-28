import math


def lexilogical_ordering(nth, zero_to):
    if zero_to >= 10:
        raise Exception('ZERO_TO_CANNOT_BE_BIGGER_THAN_10')

    nth -= 1
    digit_offsets = []
    digits = list(range(zero_to + 1))

    for digit in reversed(digits):
        factorial = math.factorial(digit)
        digit_offsets.append(int(math.floor(nth / factorial)))
        nth %= factorial

    answer_digits = [digits.pop(nth_digit) for nth_digit in digit_offsets]
    return ''.join(map(str, answer_digits))


def q24():
    nth = 1000000
    zero_to = 9

    return lexilogical_ordering(nth, zero_to)


if __name__ == '__main__':
    print(q24())
