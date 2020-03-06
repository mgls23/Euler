def is_concatenated_product_pandigital(number):
    unique_numbers = set(str(number))

    if len(unique_numbers) == 4:
        unique_numbers |= set(str(number * 2))
        unique_numbers.discard('0')
        if len(unique_numbers) == 9:
            return str(number) + str(number * 2)


# Elegant - but train-wreck
def is_concatenated_product_pandigital_one_liner(number):
    if len(set(str(number)) | set(str(number * 2)) - {'0'}) == 9: return str(number) + str(number * 2)


def q38():
    # upper_range = 9876  # have to use digits only once, and bigger the numbers in higher digit, the better
    # https://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/
    # If third digit is >= 5, we will get carry (so it will be 19, and 9 has been used)
    upper_range = 9487
    lower_range = 9182  # 9 will yield 9, 18, 2(7) => 9182

    return next(filter(is_concatenated_product_pandigital, range(upper_range, lower_range - 1, -1)))
