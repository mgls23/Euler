from itertools import combinations

from euler.util.decorators import timed_function


def right_is_bigger(tuple_sized_2):
    return tuple_sized_2[0] <= tuple_sized_2[1]


def q39(upper_bound_perimeter=1000):
    max_solution, max_perimeter = 0, -1
    for perimeter in range(4, upper_bound_perimeter + 1):
        number_of_solutions = 0
        for a, b in filter(right_is_bigger, combinations(range(1, (perimeter + 1) // 2), 2)):
            c = perimeter - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                number_of_solutions += 1

        if number_of_solutions > max_solution:
            max_perimeter, max_solution = perimeter, number_of_solutions

    return max_perimeter


if __name__ == '__main__':
    assert (timed_function(q39)(120) == 120)
    assert (timed_function(q39)() == 840)
