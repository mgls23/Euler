def champernownes_constant(n):
    digit = 1
    upper_limit = 9

    while n > upper_limit:
        digit += 1
        n -= upper_limit
        upper_limit = digit * (10 ** digit - 10 ** (digit - 1))

    n -= 1

    remainder = n // digit
    original_number = (10 ** (digit - 1)) + remainder
    digit_index = n % digit

    return int(str(original_number)[digit_index])


def brute_force():
    from functools import reduce
    from operator import mul

    decimal = ''.join(map(str, range(1000000)))
    return reduce(mul, map(lambda power: decimal[10 ** power], range(7)))
