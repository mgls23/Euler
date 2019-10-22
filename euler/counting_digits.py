import math


def brute_force(up_to, digit):
    answer = [0] * int(math.floor(math.log10(up_to)) + 1)
    for number in range(up_to + 1):
        for nth_digit, char in enumerate(reversed(str(number))):
            if int(char) == digit:
                answer[nth_digit] += 1
                # if nth_digit == 2:
                #     print(number)

    return answer


def investigate_1():
    inputs = [
        # 9
        # , 99
        # , 999
        # , 1512
        # , 1521
        # , 1121
        # , 9999
        999999999
        , 99999999999
    ]

    # for input_ in inputs:
    #     # correct = list(reversed(brute_force(input_, 1)))
    #     attempt = crude_function(input_, 1)
    #     print(f'{input_}')
    #     # print(f'C={correct}')
    #     print(f'A={attempt}')

    cumulative = 0
    for i in range(1, 100000000):
        # correct = list(reversed(brute_force(input_, 1)))
        attempt = crude_function(i, 1)
        if sum(attempt) == i:
            cumulative += sum(attempt)
            print(f'Number={i}, A={attempt}, Cumulative={cumulative}')


def crude_function(up_to, digit_compared):
    answer = [0] * int(math.floor(math.log10(up_to)) + 1)
    string = str(up_to)
    for index, digit_char in enumerate(string):
        digit_index = len(string) - index - 1
        power = int(math.pow(10, digit_index))

        digits_after = int(string[index + 1:] or 0)
        digits_before = int(string[:max(index, 0)] or 0)

        if int(digit_char) == digit_compared:
            answer[index] = digits_after + 1
            if index > 0:
                answer[index] += digits_before * power
        elif int(digit_char) > digit_compared:
            answer[index] = (digits_before + 1) * power
        elif int(digit_char) < digit_compared:
            answer[index] = digits_before * power

    return answer
