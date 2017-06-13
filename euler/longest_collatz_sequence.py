import math

# If the number is a power of 2, we know how this would be
COLLATZ_SEQUENCE = {
    int(math.pow(2, index - 1)): index
    for index in range(1, 1000)
}


def collatz_length(number):
    assert number > 0, ""

    count = 0
    sequence = []

    while number not in COLLATZ_SEQUENCE:
        sequence.append(number)

        if number == 1: break

        # Next Collatz Sequence
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = 3 * number + 1

        count += 1

    length = COLLATZ_SEQUENCE[number] + count

    for index, starting_number in enumerate(sequence[1:], 1):
        COLLATZ_SEQUENCE[starting_number] = length - index

    return length
