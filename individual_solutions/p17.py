import logging
from euler.util.decorators import timed_function

SINGLE_DIGITS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

TEEN_EXCEPTION = {
    10: "ten",
    11: "eleven",
    12: "twelve",
}

TEEN_PREFIX = SINGLE_DIGITS.copy()
TEEN_PREFIX.update({
    3: "thir",
    5: "fif",
})

TY_PREFIX = SINGLE_DIGITS.copy()
TY_PREFIX.update({
    2: "twen",
    3: "thir",
    4: "for",
    5: "fif",
})


def remove_spaces_and_hyphens(string):
    return string.replace(' ', '').replace('-', '')


def convert_to_string(number: int):
    assert 0 < number < 10000, number
    if number in SINGLE_DIGITS:
        return SINGLE_DIGITS[number]

    digit_10 = number % 100 // 10
    digit_1 = number % 10

    string = []
    if digit_1000 := number % 10000 // 1000:
        string.append(f'{SINGLE_DIGITS[digit_1000]}-thousand')

    if digit_100 := number % 1000 // 100:
        string.append(f'{SINGLE_DIGITS[digit_100]}-hundred')

        if digit_10 or digit_1: string.append(' and ')

    if digit_10 >= 2:
        string.append(add_suffix(TY_PREFIX[digit_10], "ty"))

        if digit_1: string.append('-')

    if digit_10 == 1:
        if number % 100 in TEEN_EXCEPTION:
            string.append(TEEN_EXCEPTION[number % 100])
        else:
            string.append(add_suffix(TEEN_PREFIX[digit_1], "teen"))

    elif digit_1:
        string.append(SINGLE_DIGITS[digit_1])

    return ''.join(string)


def number_letter_counts(number: int):
    string = convert_to_string(number)
    character_count = len(remove_spaces_and_hyphens(string))

    logging.debug(f'Number={number}, raw_string={string}, length={character_count}')
    return character_count


def add_suffix(string, suffix):
    """ e.g. eigh(t) + [t]y => eighty """
    return string + suffix[1:] if string[-1] == suffix[0] else string + suffix


def q17(start=1, up_to=1000):
    return sum(map(number_letter_counts, range(start, up_to + 1)))


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert (timed_function(q17)() == 21124)
