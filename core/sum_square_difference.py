# Q6 :: Sum Square Difference
def q6(n=100):
    """
    (1 + 2 + 3 + ... n)^2
     = ((n * (n + 1)) / 2) ^ 2

    1^2 + 2^2 + 3^2 + ... n^2
     [BRUTE FORCE]

        Args
        ----
            n: int

        Returns
        -------

    """
    square_of_sum = ((n + 1) * n / 2) ** 2
    sum_of_square = sum([i ** 2 for i in range(n + 1)])
    return square_of_sum - sum_of_square


if __name__ == '__main__':
    print q6()
