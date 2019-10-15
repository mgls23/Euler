import math

memoised = {}


def digit_sum(power=5):
    answers = []
    upper_limit = 354294

    for number in range(2, upper_limit):
        powers = []
        for digit in [int(digit) for digit in str(number)]:
            if digit not in memoised:
                memoised[digit] = math.pow(digit, power)

            powers.append(memoised[digit])

        sum_ = sum(powers)
        if sum_ == number:
            answers.append(number)

    return sum(answers)
