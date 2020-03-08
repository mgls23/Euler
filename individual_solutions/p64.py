from euler.util.decorators import timed_function


def q64(up_to=10 ** 4):
    odd_numbered_period_counts = 0
    for number in range(2, up_to):
        if not (number ** 0.5).is_integer():
            a0, period = find_fraction_representation_of_root(number)
            # print(f'√{number}=({a0};{period})')
            if len(period) % 2 == 1:
                odd_numbered_period_counts += 1

    return odd_numbered_period_counts


# TODO :: Should be improved
def is_repeating(array):
    if array.count(array[0]) == len(array): return [array[0]]
    for length in range(2, len(array) // 2):
        if array[:length] == array[length:length * 2]:
            return array[:length]

    return False


def find_fraction_representation_of_root(number):
    root_of_number = number ** 0.5
    a0 = int(root_of_number)

    periods = []

    before_top_number = 1
    before_bottom_number = -a0

    combinations_used = {(before_top_number, before_bottom_number)}

    for _ in range(1000):
        after_top = root_of_number - before_bottom_number
        after_bottom = number - (before_bottom_number ** 2)  # evaluated
        after_cancelled_bottom = after_bottom / before_top_number

        a = int(after_top // after_cancelled_bottom)
        periods.append(a)

        before_top_number = int(after_cancelled_bottom)
        before_bottom_number = int(-before_bottom_number - (after_cancelled_bottom * a))

        new_combination_used = (before_top_number, before_bottom_number)
        if new_combination_used in combinations_used:
            return 10, periods


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # assert (timed_function(find_fraction_representation_of_root)(23) == (4, [1, 3, 1, 8]))
    assert (timed_function(q64)(13 + 1) == 4)

    assert (timed_function(q64)() == 1322)
