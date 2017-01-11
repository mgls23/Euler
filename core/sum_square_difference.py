def sum_square_difference(n):
    """
    (1 + 2 + 3 + ... n)^2
     = ((n * (n + 1)) / 2) ^ 2

    1^2 + 2^2 + 3^2 + ... n^2
     [BRUTE FORCE]

        Args
        ----
            :param n: int

        Returns
        -------

    """
    square_of_sum = ((n + 1) * n / 2) ** 2
    sum_of_square = sum([i ** 2 for i in range(n + 1)])
    return square_of_sum - sum_of_square


# Q6 :: Sum Square Difference
def q6():
    return sum_square_difference(100)


if __name__ == '__main__':
    print q6()
