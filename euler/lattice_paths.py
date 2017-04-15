def lattice_paths(n):
    """ Triangle number with 'various degrees'

    Memory :: n
    Complexity :: n^2

    TODO :: extend for max(n, m) where it supports a rectangle rather than
    a square

    :param n: int
    :return:
    """
    initial_list = [1] * (n + 1)
    for _ in range(n):
        for index in range(1, n + 1):
            initial_list[index] += initial_list[index - 1]

    return initial_list[-1]

