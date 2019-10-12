import math


def q34():
    factorial_memoize_dict = {}
    answer = []

    # factorial(9) = 362880
    # factorial(9) * 8 = 2903040 < 10,000,000
    # factorial(9) * 7 = 2540160
    # factorial(9) * 6 + 2 = 2177282
    # Therefore upper range is 2177282 - we could go further
    for number in range(2177282):
        digits = [int(digit_str) for digit_str in str(number)]
        factorial_sum = 0
        for digit in digits:
            if digit in factorial_memoize_dict:
                factorial = factorial_memoize_dict[digit]
            else:
                factorial = math.factorial(digit)
                factorial_memoize_dict[digit] = factorial

            factorial_sum += factorial

        if factorial_sum == number:
            answer.append(number)

    answer.remove(1)
    answer.remove(2)

    return answer


print(q34())
