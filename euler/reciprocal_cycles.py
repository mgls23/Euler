def string_division(divisor, dividend=1):
    dividends = []
    quotients = []

    while dividend > 0:
        if dividend >= divisor:
            for start, number in enumerate(dividends):
                if number == dividend:
                    return len(quotients) - start

            quotients.append(int(dividend / divisor))
            dividends.append(dividend)
            dividend %= divisor

        else:
            quotients.append(0)
            dividends.append(dividend)

        dividend *= 10

    return 0


if __name__ == '__main__':
    print(q26())
