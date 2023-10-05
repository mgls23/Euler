import itertools
import logging
from operator import add, mul, sub, truediv

from euler.util.decorators import timed_function


def find_combinations(numbers):
    operators = [add, sub, mul, truediv]
    chosen = []
    results = {0}

    def helper():
        if len(chosen) == 3:
            first = chosen[0](permutation[0], permutation[1])
            second = chosen[1](first, permutation[2])
            result = chosen[2](second, permutation[3])

            # logging.debug(f'{result, permutation, chosen}')

            if result % 1 == 0:
                results.add(abs(int(result)))

            return

        for operator in operators:
            chosen.append(operator)
            helper()
            chosen.pop()

    for permutation in map(list, itertools.permutations(numbers)):
        helper()

    # logging.debug(f'{numbers, list(sorted(results))}')
    for should_be, element in enumerate(sorted(results)):
        if element != should_be:
            return should_be - 1

    return -1


def q93():
    max_permutation, max_ways = [], 0
    for permutation in map(list, itertools.combinations(range(3, 20), 2)):
        permutation = [1, 2] + permutation
        ways = find_combinations(permutation)
        if ways >= max_ways:
            logging.debug(f'{ways, permutation}')
            max_ways = ways
            max_permutation = permutation

    return ''.join(map(str, max_permutation))


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q93)() == '1258')
