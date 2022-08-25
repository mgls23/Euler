from functools import reduce
from math import gcd, sqrt

from euler.util.decorators import timed_function


# TODO :: after q9 is re-implemented after learning Euclidean formula - revisit this also
#  This somewhat touches co-prime a,b - but the 'correct' answer seems much neater
def q39(upper_bound_perimeter=1000):
    # Exploits that k* a**2 + k* b ** 2 = k* c ** 2
    # Also relies on having 1 unique pair of a, b that satisfies
    # `c ** 2 = a ** 2 + b ** 2` - which I'm not sure is proven, but it seems unlikely
    possibilities = list(fits_fibonacci(upper_bound_perimeter))
    valid_perimeters = list(map(sum, possibilities))
    assert (len(possibilities) == len(valid_perimeters))

    max_solution, max_perimeter = 0, -1
    # https://projecteuler.net/thread=39 @rayfil::P will always be even
    for perimeter in range(4, upper_bound_perimeter + 1, 2):
        solution = len([1 for valid_perimeter in valid_perimeters if perimeter % valid_perimeter == 0])
        if solution > max_solution:
            max_solution, max_perimeter = solution, perimeter

    return max_perimeter


def fits_fibonacci(max_perimeter=1000):
    possible = []

    # b is the bigger side (than a), and c is hypotenuse
    for bigger_leg in range(1, max_perimeter // 2):
        for smaller_leg in range(1, bigger_leg + 1):
            hypotenuse = sqrt(smaller_leg ** 2 + bigger_leg ** 2)
            if hypotenuse.is_integer() and reduce(gcd, [smaller_leg, bigger_leg, int(hypotenuse)]) == 1:
                possible.append((smaller_leg, bigger_leg, int(hypotenuse)))

    return possible


if __name__ == '__main__':
    timed_function(fits_fibonacci)()

    # assert (timed_function(q39)(120) == 120)
    # assert (timed_function(q39)() == 840)
