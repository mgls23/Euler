import math


def brute_force(up_to, digit):
    answer = [0] * int(math.floor(math.log10(up_to)) + 1)
    for number in range(up_to + 1):
        for nth_digit, char in enumerate(reversed(str(number))):
            if int(char) == digit:
                answer[nth_digit] += 1

    return answer


def investigate_1():
    # inputs = [
    #     9
    #     , 99
    #     , 999
    #     , 1512
    #     , 1521
    #     , 1121
    #     , 9999
    #     , 999999999
    #     , 99999999999
    # ]

    # for input_ in inputs:
    #     correct = list(reversed(brute_force(input_, 1)))
    #     attempt = count_digit_occurence_until(input_, 1)
    #     if correct != attempt:
    #         print(f'{input_}')
    #         print(f'Correct={correct}')
    #         print(f'Attempt={attempt}')

    all_answers = []
    cumulative = 0
    n = 1
    add_by = 1

    last_difference = 0
    last_number = 1

    while True:
        result = sum(count_digit_occurence_until(n, 1))
        this_difference = n - result
        if abs(this_difference) > abs(last_difference):
            print(f'Difference becoming bigger::Result={result}, n={n}, this={this_difference}, last={last_difference}')
            cumulative = find_in_range(last_number, n, cumulative, all_answers)

        if result == n:
            cumulative += result
            all_answers.append(result)
            print(f'Number={n}, A={result}, Cumulative={cumulative}')

            cumulative = find_in_range(last_number, n, cumulative, all_answers)

        last_difference = this_difference

        if n > math.pow(10, 6): break
        last_number = n
        n += add_by
        add_by = max(n // 10, add_by)

    print(f'All Answers={all_answers}')
    return cumulative


def find_in_range(lower, upper, cumulative, all_answers):
    print(f'find_in_range({lower}, {upper})')
    for n in range(lower, upper):
        result = sum(count_digit_occurence_until(n, 1))
        if result == n:
            cumulative += result
            all_answers.append(result)
            print(f'Number={n}, A={result}, Cumulative={cumulative}')

    return cumulative


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
