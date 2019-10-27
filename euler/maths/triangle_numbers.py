import math

from euler.util.decorators import memoised


@memoised
def is_triangle_number(number):
    if number <= 0: return False
    return check_is_integer_and_odd(triangular(number))


def triangular(number):
    # Used for triangularity check
    return math.sqrt((number * 8) + 1)


def is_pentagonal_number(number):
    if number <= 0: return False
    return check_is_integer_and_odd(pentagonal(number))


def pentagonal(number):
    return math.sqrt(12 * number ** 2 - 4 * number + 1)


def hexagonal(number):
    return math.sqrt(16 * number ** 2 - 8 * number + 1)


def check_is_integer_and_odd(number):
    return number.is_integer() and number % 2 == 1
