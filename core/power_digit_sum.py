# Q16 :: Digit of 2^1000
def q16(power=15):
    """
    1, 2, 4, 8, 16, 32, 64, 128, ...


        Args
        ----
            power

        Returns
        -------
    """
    assert power > 0, "Please provide a number bigger than 0 " \
                      "so we can do some cool maths"

    number_array_repr = [1]
    for i in range(power):
        for j in range(len(number_array_repr)):
            number_array_repr[j] *= 2

        for index in range(len(number_array_repr)):
            while number_array_repr[index] >= 10:
                number_array_repr[index] -= 10
                try:
                    number_array_repr[index + 1] += 1

                except IndexError:
                    number_array_repr.append(1)

    return sum(number_array_repr)
