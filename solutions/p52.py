from solutions.euler.util.decorators import timed_function


def q52(consecutive=6):
    # 1 * 6 = 6 :: minimum is 100,000
    for number1_digit in range(5, 100000):
        # 2 * 6 = 12 => increases digit. First digit *has* to be 1
        for number1 in range(10 ** number1_digit, 2 * 10 ** number1_digit):
            number1_string_set = set(str(number1))
            for multiplier in range(2, consecutive + 1):
                number2_string = str(number1 * multiplier)
                if len(number2_string) > len(number1_string_set): break

                number2_string_set = set(number2_string)
                if len(number2_string) != len(number1_string_set) or number1_string_set != number2_string_set: break

            else:
                return number1


if __name__ == '__main__':
    assert (timed_function(q52)() == 142857)
