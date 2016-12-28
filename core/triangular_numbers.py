def find_all_factors(number):
    factors = []
    for index in range(1, number + 1):
        if number % index == 0:
            factors.append(index)

    return factors


def spam():
    for index in range(1, 100):
        triangle_number = index * (index + 1) / 2
        triangle_number_factors = find_all_factors(triangle_number)
        print '%(triangle_number)s: %(triangle_number_factors)s' % locals()


if __name__ == '__main__':
    spam()
