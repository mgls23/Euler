import logging
import math

from euler.util.fibonacci import FibonacciIterator


def slow_attempt(digit):
    iterator = FibonacciIterator()
    iterator.set_upper_bound(10 ** (digit - 1))

    last_digit = 0
    digits_items = []
    for iteration, fibonacci_term in enumerate(iterator.sequence):
        digit = int(math.log10(fibonacci_term))
        if digit > last_digit:
            logging.debug('{} broken, because digit {} > {}, cause::{}'.format(
                digits_items, digit, last_digit, fibonacci_term))

            last_digit = digit
            digits_items = []
        else:
            digits_items.append(fibonacci_term)

    # logging.debug('Sequence::{}'.format(iterator.sequence))
    # +1 because our iterator does not include 1, and +1 because we've set the upper limit
    # to 10 ** 1000
    return len(iterator.sequence) + 1 + 1
