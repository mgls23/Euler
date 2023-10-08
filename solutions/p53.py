from math import factorial

from .euler.util.decorators import timed_function


# If this extended (such that ncr_requirement can be smaller than n, this function will need to be modified
def find_first_non_fitting_r(n, ncr_needs_to_be, starting_r):
    top = factorial(n) // factorial(n - starting_r)  # Special optimisation in factorial is fast
    bottom = factorial(starting_r)
    ncr = top // bottom

    for r in range(starting_r, 0, -1):
        if ncr < ncr_needs_to_be:
            return r

        ncr *= r
        ncr /= (n - r + 1)


# Optional :: Implement this in Pascal's Triangle.
#   This is "better" version of Pascal's Triangle which uses symmetry to cut calculation by half
#   and uses less memory - Pascal's Triangle is simpler. Also - I could "reuse" factorial generated
def q53(upper_range=100, ncr_requirement=10 ** 6):
    fitting_ncr_combinations = 0
    r_boundary = 23 // 2 - 1

    # question stated first instance of n is 23
    for n in range(23, upper_range + 1):
        r_boundary = find_first_non_fitting_r(n, ncr_requirement, r_boundary + 1)

        # No need to check if non_fitting_r is != n // 2
        fitting_ncr_combinations += (n // 2 - r_boundary) * 2
        if n % 2 == 0: fitting_ncr_combinations -= 1

    return fitting_ncr_combinations


if __name__ == '__main__':
    assert (timed_function(q53)() == 4075)
