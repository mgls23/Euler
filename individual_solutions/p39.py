from functools import reduce
from math import gcd, sqrt

from euler.util.decorators import timed_function


def q39(upper_bound_perimeter=1000):
    # Exploits that k* a**2 + k* b ** 2 = k* c ** 2
    # Also relies on having 1 unique pair of a, b that satisfies
    # `c ** 2 = a ** 2 + b ** 2` - which I'm not sure is proven, but it seems unlikely
    possibilities = list(fits_fibonacci(upper_bound_perimeter))
    valid_perimeters = list(map(sum, possibilities))
    assert (len(possibilities) == len(valid_perimeters))

    max_solution, max_perimeter = 0, -1
    for perimeter in range(4, upper_bound_perimeter + 1):
        solution = len([1 for valid_perimeter in valid_perimeters if perimeter % valid_perimeter == 0])
        if solution > max_solution:
            max_solution, max_perimeter = solution, perimeter

    return max_perimeter


def fits_fibonacci(max_perimeter=1000):
    possible = set()

    # b is the bigger side (than a), and c is hypotenuse
    for bigger_leg in range(1, max_perimeter // 2):
        for smaller_leg in range(1, bigger_leg + 1):
            hypotenuse = sqrt(smaller_leg ** 2 + bigger_leg ** 2)
            if hypotenuse.is_integer():
                triangle_gcd = reduce(gcd, [smaller_leg, bigger_leg, int(hypotenuse)])
                possible.add((smaller_leg // triangle_gcd, bigger_leg // triangle_gcd, int(hypotenuse) // triangle_gcd))

    return possible


if __name__ == '__main__':
    assert (timed_function(q39)(120) == 120)
    assert (timed_function(q39)() == 840)
