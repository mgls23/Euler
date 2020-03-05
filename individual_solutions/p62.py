from collections import Counter

from euler.sequence.polynomial import Polynomial
from euler.util.decorators import timed_function


def q62(number_of_matches=5):
    cube_generator = Polynomial(3)

    for digit_estimated in range(8, 20):
        cube_numbers = cube_generator.generate_numbers_with(digit_estimated)

        tuples = [(''.join(sorted(str(cube_number))), cube_number) for cube_number in cube_numbers]
        strings_counted = Counter([number_string for number_string, number in tuples])
        matches = [sorted_string for sorted_string, matches in strings_counted.items() if matches == number_of_matches]
        if matches:
            logging.debug([number for string_number, number in tuples if string_number in matches])
            return min([number for string_number, number in tuples if string_number in matches])


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q62)() == 127035954683)
