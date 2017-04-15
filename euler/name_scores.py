MAX_LENGTH = 12

BASE_SCORE = ord('A') - 1
BASE_SCORES = [BASE_SCORE * index for index in range(MAX_LENGTH)]


def calculate_score(string):
    """Calculates the numerical score of a given string
    The score of each character the string is its ordinal value

    a=1, b=2, z=26
    """
    cumulative = sum([ord(character) for character in string])
    return cumulative - BASE_SCORES[len(string)]
