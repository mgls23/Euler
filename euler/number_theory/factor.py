""" Just copied structure of sympy - I can update """


def sigma_totient(lower, upper):
    visited = list(range(upper + 1))
    summed = 0

    for index in range(lower, upper + 1):  # don't use enumerate/iterator
        # Prime Number
        if index == visited[index]:
            summed += index - 1

            # reverse - sieve: decrease by (p-1)/p
            for to_update in range(index * 2, upper + 1, index):
                visited[to_update] *= (index - 1) / index

        # Composite / power - already decreased
        else:
            summed += visited[index]

    return int(summed)
