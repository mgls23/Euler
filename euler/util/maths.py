import math


def fizz_buzz(x, lower_bound=2, fizz=3, buzz=5):
    """ Finds all multiples of 3s and 5s until the given number

    :param x :int (The upper bound to perform fizz buzz on)
    :param lower_bound :int
    :param fizz :int
    :param buzz :int
    """
    return [number
            for number in range(lower_bound, x + 1)
            if (number % fizz) == 0 or (number % buzz) == 0]


def guassian_sum(upper_bound, multiplier):
    """ Finds multiplicative sum [pi] of multiplicand no bigger than the upper bound.
    The multiplication with multiplicand x 1, therefore it does not include 0

    This uses a simple property that 1 + 2 + 3 + 4 + 5 ... + (n-1) + n = (n + 1) x n/2
    Taking the example of multiplicand of 3,
    3 + 6 + 9 + 12 + 15 + ... 3n
        = 3 x 1 + 3 x 2 + 3 x 3 + ... 3 x n
        = 3 x (1 + 2 + 3 + ... n)
        = 3 x (n + 1) x n/2
        = m * (n + 1) x n/2
         [m being the multiplicand]

    Do note that n will be the highest multiple of multiplicand smaller than upper bound
        :: n = math.floor(upper_bound / multiplicand

    :param upper_bound :int
    :param multiplier :int
    """
    # Catch negative n cases as well as 0 case here
    if upper_bound < multiplier: return 0

    n = math.floor(upper_bound / multiplier)
    return multiplier * (n + 1) * n / 2
