from .euler.util.decorators import timed_function


def continued_fraction_has_odd_periods(number):
    # https://projecteuler.net/thread=64 - mathgod optimisation
    always_true_offset = [+1]
    always_false_offset = [-1, -2, 0, +2]
    if any(((number - offset) ** 0.5).is_integer() for offset in always_true_offset): return True
    if any(((number - offset) ** 0.5).is_integer() for offset in always_false_offset): return False

    a0, period = find_fraction_representation_of_root(number)
    # print(f'√{number}=({a0};{period})')
    return len(period) % 2 == 1


def q64(up_to=10 ** 4):
    numbers_with_odd_periods = [number for number in range(2, up_to) if continued_fraction_has_odd_periods(number)]
    return len(numbers_with_odd_periods)


def find_fraction_representation_of_root(number):
    root_of_number = number ** 0.5
    a0 = int(root_of_number)

    periods = []

    # Before indicates before expanded (because the fraction reverses)
    # It is only necessary to keep track of the number because the root number stays constant
    before_top_number = 1
    before_bottom_number = -a0

    expanded = {(before_top_number, before_bottom_number)}

    for _ in range(1000):
        after_top = root_of_number - before_bottom_number
        after_bottom = (number - (before_bottom_number ** 2)) / before_top_number

        a = int(after_top // after_bottom)
        periods.append(a)

        before_top_number = int(after_bottom)
        before_bottom_number = int(-before_bottom_number - (after_bottom * a))

        expand_next = (before_top_number, before_bottom_number)
        if expand_next in expanded:
            return a0, periods


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(find_fraction_representation_of_root)(23) == (4, [1, 3, 1, 8]))
    assert (timed_function(q64)(13 + 1) == 4)

    assert (timed_function(q64)() == 1322)
