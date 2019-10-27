def sigma_n(n):
    # 1 + 2 + 3 ... n
    # sigma(i) i=[1..n]
    # = (n+1) x n /2
    return (n + 1) * n / 2


def sigma_n2(n):
    # 1**2 + 2**2 + ... n**2 =
    # sigma(i^2) i=[1..n]
    # = n(n + 1)(2n + 1) / 6
    return n * (n + 1) * (2 * n + 1) / 6
