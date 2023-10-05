# TODO :: Re-implement Pythagoras with Euclidean formula
def q9(perimeter=1000):
    for a in range(perimeter // 2):
        for b in range(a):
            c = perimeter - a - b

            if a * a + b * b == c * c:
                return a * b * c

    raise Exception('NOTHING_FOUND')
