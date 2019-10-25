import math

from euler.util.decorators import memoised


@memoised
def is_triangle_number(number):
    if number <= 0: return False
    x = math.sqrt((number * 8 + 1))
    return x.is_integer() and x % 2 == 1
