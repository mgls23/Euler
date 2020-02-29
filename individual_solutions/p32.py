from itertools import combinations

from euler.util.decorators import timed_function


def is_partial_pandigital(number):
    number_string = str(number)
    return len(set(number_string) - {'0'}) == len(number_string)


def is_pandigital_product(x, y):
    string_x, string_y = str(x), str(y)
    unique_numbers = set(string_x) | set(string_y)
    if len(unique_numbers) == len(string_x) + len(string_y):  # duplicating checks for worthwhile speedup
        product_string = str(x * y)
        unique_numbers |= set(product_string)
        unique_numbers.discard('0')
        return len(unique_numbers) == 9 == len(string_x) + len(string_y) + len(product_string)


def q32():
    pan_digitals = set()

    for x, y in combinations(list(filter(is_partial_pandigital, range(10 ** 3))), 2):
        if is_pandigital_product(x, y):
            pan_digitals.add(x * y)

    # handle 1 digit x 4 digit
    for y in filter(is_partial_pandigital, range(10 ** 4)):
        for x in range(1, 10):
            if is_pandigital_product(x, y):
                pan_digitals.add(x * y)

    return sum(pan_digitals)


if __name__ == '__main__':
    assert (timed_function(q32)() == 45228)
