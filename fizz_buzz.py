def fizz_buzz(x):
    """
    Finds all multiples of 3s and 5s until the given number

    Parameters
    ----------
    x:  Int
        The upper bound to perform fizz buzz on. See @Doc

    Returns
    -------

    """
    if x <= 2:
        return []

    found = []
    for index in range(x):
        div3 = index % 3
        div5 = index % 5
        if div3 == 0 or div5 == 0:
            found.append(index)

    return found
