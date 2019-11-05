from euler.util.decorators import memoised


@memoised
def f(n):
    if n <= 1: return n

    sum_ = 1
    for i in range(n, 0, -1):
        reverse = n - i
        if 1 <= reverse <= (n // 2):
            sum_ += f(reverse)
        else:
            sum_ += _f(reverse, i)

    return sum_


@memoised
def _f(n, m):
    if n <= 1: return n
    if m >= n: return f(n)

    sum_ = 1
    for i in range(m, 1, -1):
        reverse = n - i
        if 1 <= reverse <= (n // 2):
            sum_ += f(reverse)
        else:
            sum_ += _f_(reverse, i)

    return sum_


@memoised
def _f_(n, m):
    if n <= 1: return n
    if m == 1: return 1

    sum_ = 1  # i = 1
    for i in range(2, m + 1):
        for j in range(i, (n // i) * i + 1, i):
            sum_ += _f(n - j, i - 1)
        sum_ += (n % i) == 0 and 1 or 0

    return sum_
