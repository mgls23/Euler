BASE_STARTS_WITH_1 = ord('A') - 1


def numerical_score(string):
    """Calculates the numerical score of a given string
    The score of each character the string is its ordinal value

    Only tested with capital letters

    A=1, B=2, Z=26
    """
    return sum(ord(char) for char in string) - BASE_STARTS_WITH_1 * len(string)
