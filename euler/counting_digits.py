import math
import matplotlib.pyplot as plt


def brute_force(up_to, digit):
    answer = [0] * int(math.floor(math.log10(up_to)) + 1)
    for number in range(up_to + 1):
        for nth_digit, char in enumerate(reversed(str(number))):
            if int(char) == digit:
                answer[nth_digit] += 1

    return answer


def investigate():
    cumulative = 0
    for d in range(1, 9 + 1):
        inputs, answers = [], []
        for n in range(1, 5000000):
            raw_answer = count_digit_occurence_until(n, d)
            answer = sum(raw_answer)
            if answer == n:
                cumulative += answer
                print(f'Number={n}, A={raw_answer}, Cumulative={cumulative}')

            inputs.append(n)
            answers.append(answer)

        print(f'Digit {d} done')
        plt.figure(d)
        plt.plot(inputs, inputs)
        plt.plot(inputs, answers)
        plt.show()


def investigate_1(digit_investigated=3):
    # inputs = [
    #     9
    #     , 99
    #     , 999
    #     , 1512
    #     , 1521
    #     , 1121
    #     , 9999
    # ]
    #
    # for input_ in inputs:
    #     correct = list(reversed(brute_force(input_, digit_investigated)))
    #     attempt = count_digit_occurence_until(input_, digit_investigated)
    #     if correct != attempt:
    #         print(f'{input_}')
    #         print(f'Correct={correct}')
    #         print(f'Attempt={attempt}')
    #     else:
    #         print(f'Input={input_} generated {sum(correct)} correctly')

    inputs, answers = [], []

    cumulative = 0
    for n in range(1, 5000000):
        raw_answer = count_digit_occurence_until(n, digit_investigated)
        answer = sum(raw_answer)
        if answer == n:
            cumulative += answer
            print(f'Number={n}, A={raw_answer}, Cumulative={cumulative}')

        inputs.append(n)
        answers.append(answer)

    plt.plot(inputs, inputs)
    plt.plot(inputs, answers)
    plt.show()


def count_digit_occurence_until(up_to, digit_compared):
    answer = [0] * int(math.floor(math.log10(up_to)) + 1)
    string = str(up_to)
    for index, digit_char in enumerate(string):
        digit_index = len(string) - index - 1
        power = int(math.pow(10, digit_index))

        digits_before = int(string[:max(index, 0)] or 0)

        if int(digit_char) == digit_compared:
            digits_after = int(string[index + 1:] or 0)
            answer[index] = digits_after + 1
            if index > 0:
                answer[index] += digits_before * power
        elif int(digit_char) > digit_compared:
            answer[index] = (digits_before + 1) * power
        elif int(digit_char) < digit_compared:
            answer[index] = digits_before * power

    return answer
