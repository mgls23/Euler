def power_digit_sum(power, starting_number=1, multiplier=2):
    """ Finds the sum of the digits 
    :power: int
    :starting_number: int
    :multiplier: int"""
    assert power > 0, "Please provide a number bigger than 0 as the power"

    decimal_digits = [starting_number]
    for _ in range(power):
        for index in range(len(decimal_digits)):
            decimal_digits[index] *= multiplier

        for index in range(len(decimal_digits)):
            while decimal_digits[index] >= 10:
                decimal_digits[index] -= 10
                try:
                    decimal_digits[index + 1] += 1

                except IndexError:
                    decimal_digits.append(1)

    decimal_digits.reverse()
    return sum(decimal_digits)


# Q16 :: Digit of 2^1000
def q16():
    return power_digit_sum(1000)


if __name__ == '__main__':
    print(q16())
