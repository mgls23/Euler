# TODO :: Refactor
import logging


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
            logging.debug('Before :: current_sum=%(current_sum)s' % locals())
            logging.debug('index  :: {}'.format(number[index]))
            current_sum += int(number[index])
            logging.debug('After  :: current_sum=%(current_sum)s' % locals())

        if current_sum != 0:
            current_digit = current_sum % 10
            logging.debug(
                'Before :: ' \
                'current_digit=%(current_digit)s, ' \
                'current_sum=%(current_sum)s' % locals()
            )
            final_accumulated_in_reverse.append(str(current_digit))

        current_sum /= 10
        logging.debug('After  :: current_digit=%(current_digit)s, ' \
            'current_sum=%(current_sum)s' % locals()
        )

    remaining = list(str(current_sum))
    logging.debug('current_sum=%(current_sum)s, ' \
                  'remaining=%(remaining)s' % locals())

    if len(remaining) > 0 and current_sum > 0:
        remaining.reverse()
        final_accumulated_in_reverse += remaining

    final_accumulated_in_reverse.reverse()
    final_sum = ''.join(final_accumulated_in_reverse[:first_digits])

    return desired_type(final_sum)
