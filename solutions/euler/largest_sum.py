def first_n_digits_of_sum(first_digits, numbers, output_type=int):
    """Assumes that the length of numbers are equal

    :param first_digits:int
    :param numbers: list
    :param output_type: type
    """
    accumulates = []
    carry = 0

    for string_index in range(len(numbers[0]) + 1):
        accumulate = sum(int(number[-string_index]) for number in numbers) + carry
        carry = accumulate // 10
        accumulates.append(accumulate % 10)

    while carry > 0:
        accumulates.append(carry % 10)
        carry //= 10

    accumulates.reverse()
    final_sum = ''.join(map(str, accumulates))
    return output_type(final_sum[:first_digits])


def alternative(first_digits, numbers, output_type=int):
    return output_type(str(sum(map(int, numbers)))[:first_digits])
