# Q22 :: Calculating the name scores
def q22():
    names_text = open('data/p022_names.txt', 'r').readlines()[0]

    names = names_text.replace('"', '').split(',')
    names.sort()

    cumulative = 0
    for index, name in enumerate(names):
        coefficient = index + 1
        cumulative += coefficient * calculate_score(name)

    return cumulative


base = ord('A') - 1


def calculate_score(string):
    """Calculates the numerical score of a given string
    Each character the string are awarded with a scroe based on its
    ordinal value

        a = 1
        triangle_number = 2
        ...
        z = 26
    """
    cumulative = sum([ord(char) for char in string])
    return cumulative - (base * len(string))
