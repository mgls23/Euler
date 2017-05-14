import logging
import math
import sys

from euler.util.exceptions import NotSupportedException


class FibonacciIterator:
    """ FibonacciIterator that calculates and stores calculated
    fibonacci sequence values. N.B. This excludes the 1st 1

        (x) 1, 2, 3, 5, 8, 13, ...
        ( ) 1, 1, 2, 3, 5, 8, 13, ...
    """

    def __init__(self, initial_list=None):
        self.sequence = initial_list or [1, 2]

    def _calculate_next(self):
        """Calculates and stores the next Fibonacci Sequence"""
        self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def calculate_nth(self, n):
        """Calculates and returns nth fibonacci sequence"""
        if n < 1:
            raise NotSupportedException('Fibonacci Iterator needs at least 1')

        # See if that value has been calculated already
        while len(self.sequence) < n:
            self._calculate_next()

        # nth => n-1th in the list [0th of list is 1st Fibonacci]
        return self.sequence[n - 1]

    def peek(self):
        return self.sequence[-1]

    def set_upper_bound(self, upper_bound):
        if upper_bound < 1:
            raise NotSupportedException('The upper bound of Fibonacci Iterator > 1')

        while self.peek() < upper_bound:
            self._calculate_next()

        # Discard any entries that are bigger than the upper bound
        while self.peek() > upper_bound:
            self.sequence.pop(-1)

        # Return the last entry
        return self.peek()


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


def q25():
    digit = 1000
    answer = slow_attempt(digit)
    return answer


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    print(q25())
