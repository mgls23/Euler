import math


def memoised(function_, ):
    pre_computed = {}

    def wrapper(*args):
        if args not in pre_computed:
            answer = function_(*args)
            pre_computed[args] = answer

        return pre_computed[args]

    return wrapper


@memoised
def is_triangle_number(number):
    if number <= 0: return False
    x = math.sqrt((number * 8 + 1))
    return x.is_integer() and x % 2 == 1
