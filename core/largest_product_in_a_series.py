# Q8 :: Adjacent Multiplicand
def q8(x, window_size=13):
    """

    Args
    ----
        x
        window_size

    Returns
    -------

    """
    assert x and window_size, "Please provide a number that we could run " \
                              "some cool maths on"

    # Break down x into a list
    x = [int(string) for string in (type(x) == int) and str(x) or x]
    y = x[:-1]

    for iteration_count in range(1, window_size):
        for index in range(len(y) - 1):
            y[index] *= x[index + iteration_count]

        y.pop(-1)

    return max(y)
