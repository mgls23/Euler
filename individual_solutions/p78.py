def break_down(number):
    return 1 + sum(map(lambda other: break_down_with_limit(number, other), range(1, number)))


def break_down_with_limit(number, no_bigger_than):
    if no_bigger_than == 1: return 1
    return sum(map(lambda other: break_down_with_limit(number - other, other), range(1, no_bigger_than)))


def q78():
    for i in range(2, 100):
        print(f'{i}={break_down(i)}')
