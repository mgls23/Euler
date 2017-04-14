# TODO :: Refactor
def first_n_digits_of_sum(first_digits, numbers, desired_type=str):
    """
    Assumes that the lengh of numbers are equal

    :param first_digits:
    :param numbers:
    :param desired_type:
    """
    final_accumulated_in_reverse = []
    current_sum = 0

    for index in range(len(numbers[0]) - 1, -1, -1):
        for number in numbers:
            print('Before :: current_sum=%(current_sum)s' % locals())
            print('index  :: {}'.format(number[index]))
            current_sum += int(number[index])
            print('After  :: current_sum=%(current_sum)s' % locals())

        if current_sum != 0:
            current_digit = current_sum % 10
            print('Before :: ' \
                  'current_digit=%(current_digit)s, ' \
                  'current_sum=%(current_sum)s' % locals())
            final_accumulated_in_reverse.append(str(current_digit))

        current_sum /= 10
        print('After  :: ' \
              'current_digit=%(current_digit)s, ' \
              'current_sum=%(current_sum)s' % locals())

    remaining = list(str(current_sum))
    print('current_sum=%(current_sum)s, ' \
          'remaining=%(remaining)s' % locals())

    if len(remaining) > 0 and current_sum > 0:
        remaining.reverse()
        final_accumulated_in_reverse += remaining

    final_accumulated_in_reverse.reverse()
    final_sum = ''.join(final_accumulated_in_reverse[:first_digits])

    return desired_type(final_sum)


def q13():
    with open('data/p013_numbers.txt') as numbers_file:
        numbers = [
            number.replace('\n', '')
            for number in numbers_file.readlines()
        ]
        print(len(numbers))

        return first_n_digits_of_sum(10, numbers)


if __name__ == '__main__':
    print(q13())
