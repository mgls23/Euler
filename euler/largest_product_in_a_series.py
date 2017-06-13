def adjacent_multiplicand(string, window_size):
    """
    :param string :str
    :param window_size :int
    """
    assert string and window_size

    # Break down x into a list
    string = list(map(int, string))
    y = string[:-1]

    for iteration_count in range(1, window_size):
        for index in range(len(y) - 1):
            y[index] *= string[index + iteration_count]

        y.pop(-1)

    return max(y)
