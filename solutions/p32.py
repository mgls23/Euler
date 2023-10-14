from solutions.euler.util.decorators import timed_function


def is_partially_1_to_9_pandigital(number_string):
    return len(set(number_string) - {'0'}) == len(number_string)


def q32():
    total_left_digits = 5  # Only consider 5 digit numbers on LHS
    pan_digitals = set()

    numbers_in_range = range(10 ** (total_left_digits - 1), 10 ** total_left_digits)
    for left_hand_side in filter(is_partially_1_to_9_pandigital, map(str, numbers_in_range)):
        for split_index in range(0 + 1, total_left_digits - 1):
            multiplicand, multiplier = left_hand_side[:split_index], left_hand_side[split_index:]
            product_string = str(int(multiplicand) * int(multiplier))
            unique_numbers = set(left_hand_side) | set(product_string) - {'0'}

            if len(unique_numbers) == 9 == len(left_hand_side) + len(product_string):
                pan_digitals.add(product_string)

    return sum(map(int, pan_digitals))


if __name__ == '__main__':
    assert (timed_function(q32)() == 45228)
