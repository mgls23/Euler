from euler.util.decorators import timed_function


def q52(consecutive=6):
    for number1 in range(1, 10000000):
        number1_string_set = set(str(number1))
        for multiplier in range(2, consecutive + 1):
            number2 = number1 * multiplier
            number2_string = str(number2)

            if len(number2_string) > len(number1_string_set): break

            number2_string_set = set(number2_string)
            if len(number2_string) != len(number1_string_set) or number1_string_set != number2_string_set: break

        else:
            return number1


if __name__ == '__main__':
    assert (timed_function(q52)() == 142857)
