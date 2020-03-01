from math import factorial

from euler.util.decorators import timed_function


def find_first_non_fitting_r(n, ncr_needs_to_be):
    starting_r = n // 2
    top = factorial(n) // factorial(n - starting_r)  # Special optimisation in factorial is fast
    bottom = factorial(starting_r)
    ncr = top // bottom

    for r in range(starting_r, 0, -1):
        if ncr < ncr_needs_to_be:
            return r

        ncr *= r
        ncr /= (n - r + 1)


def q53(upper_range=100, ncr_requirement=10 ** 6):
    fitting_ncr_combinations = 0

    # question stated first instance of n is 23
    for n in range(23, upper_range + 1):
        non_fitting_r = find_first_non_fitting_r(n, ncr_needs_to_be=ncr_requirement)

        # No need to check if non_fitting_r is != n // 2
        fitting_ncr_combinations += (n // 2 - non_fitting_r) * 2
        if n % 2 == 0:
            fitting_ncr_combinations -= 1

    return fitting_ncr_combinations


if __name__ == '__main__':
    assert (timed_function(q53)() == 4075)
