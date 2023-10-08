import logging
from itertools import combinations

from .euler.maths.prime import generate_to_sie
from .euler.util.decorators import timed_function


def q51() -> int:
    prime_numbers = generate_to_sie(10 ** 7)

    explored = 10
    dictionary = {}
    for prime_number in prime_numbers:
        if prime_number >= explored:
            explored *= 10
            max_family = max(dictionary, key=lambda key: len(dictionary[key]))
            # print('MAX', max_format, dictionary[max_format])
            if len(dictionary[max_family]) >= 8:
                return int(max_family.replace('X', dictionary[max_family][0]))
            dictionary.clear()

        digits = list(str(prime_number))

        occurrences = dict()
        for i, character in enumerate(digits):
            if character not in occurrences: occurrences[character] = []
            occurrences[character].append(i)

        for character, indexes in occurrences.items():
            for indexes_size in range(1, len(indexes) + 1):
                for group in combinations(indexes, indexes_size):
                    for i in group: digits[i] = 'X'
                    family = ''.join(digits)
                    if family not in dictionary: dictionary[family] = []
                    dictionary[family].append(character)
                    for i in group: digits[i] = character


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    assert (timed_function(q51)() == 121313)
