from math import factorial

from euler.util.decorators import timed_function


def c(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)


def q53(upper_range=100):
    ncr_count = 0

    # question stated first instance of n is 23
    for n in range(23, upper_range + 1):
        r = n // 2
        top = factorial(n) // factorial(n - r)  # Special optimisation in factorial is fast
        bottom = factorial(r)
        ncr = top // bottom

        for r in range(r, 0, -1):
            if ncr < 10 ** 6: break

            ncr *= r
            ncr /= (n - r + 1)

        if r != n:
            if n % 2 == 0:
                ncr_count += 1 + (n // 2 - r - 1) * 2
            else:
                ncr_count += (n // 2 - r) * 2

    return ncr_count


if __name__ == '__main__':
    assert (timed_function(q53)() == 4075)
