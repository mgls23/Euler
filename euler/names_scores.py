NUMBER_TO_STRING = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

TEEN_EXCEPTION = {
    10: "ten",
    11: "eleven",
    12: "twelve",
}

TY_UPPED = {
    2: "twen",
    3: "thir",
    4: "for",
    5: "fif",
}

TEEN_UPPED = {
    2: "twen",
    3: "thir",
    5: "fif",
}


def remove_spaces_and_hyphens(string):
    return string.replace(' ', '').replace('-', '')


def translate(number):
    if number in NUMBER_TO_STRING:
        string = NUMBER_TO_STRING[number]
    else:
        string = ""

        digit_3 = number // 100
        digit_2 = number % 100 // 10
        digit_1 = number % 10

        if digit_3:
            string += NUMBER_TO_STRING[digit_3] + "-" + "hundred"

            if digit_2 or digit_1:
                string += ' and '

        if digit_2 >= 2:
            prefix = TY_UPPED.get(digit_2, NUMBER_TO_STRING[digit_2])
            string += add_suffix(prefix, "ty")

            if digit_1:
                string += "-"

        if digit_1 and digit_2 != 1:
            string += NUMBER_TO_STRING[digit_1]

        if digit_2 == 1:
            if digit_1 > 2:
                prefix = TEEN_UPPED.get(
                    digit_1, NUMBER_TO_STRING[digit_1])
                string += add_suffix(prefix, "teen")
            else:
                string += TEEN_EXCEPTION[number % 100]

    stripped_string = remove_spaces_and_hyphens(string)
    character_count = len(stripped_string)

    print(f"Number={number}, string={string}, "
          #   f"stripped_string={stripped_string}, "
          f"length={character_count}")
    return character_count


def add_suffix(string, suffix):
    if string[-1] == suffix[0]:
        return string + suffix[1:]

    return string + suffix


def test_translate(number: int, string: str, score: int):
    result = translate(number)
    stripped_string = remove_spaces_and_hyphens(string)

    assert (result == score), f"{result} != {score}"
    assert (score == len(stripped_string)), f"{score} != len({stripped_string})"


def test():
    # No need to test any entries in NUMBER_TO_STRING other than 1
    test_translate(1, "one", score=3)
    test_translate(12, "twelve", score=6)
    test_translate(14, "fourteen", score=8)
    test_translate(40, "forty", score=5)
    test_translate(100, "one-hundred", score=10)
    test_translate(256, "two-hundred and fifty-six", score=21)
