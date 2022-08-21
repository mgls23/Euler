from euler.util.exceptions import NotSupportedException


class FibonacciIterator:
    """ A wrapper for Fibonacci sequence in case the requirement changes """

    def __init__(self, initial_list=None, start_with_two_1s=False):
        if initial_list is None:
            initial_list = start_with_two_1s and [1, 1, 2] or [1, 2]

        self.sequence = initial_list

    def _calculate_next(self):
        """Calculates and stores the next Fibonacci Sequence"""
        self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def calculate_nth(self, n):
        """Calculates and returns nth fibonacci sequence"""
        if n < 1:
            raise NotSupportedException('')

        # See if that value has been calculated already
        for _ in range(n - len(self.sequence)):
            self._calculate_next()

        # nth => n-1th in the list [0th of list is 1st Fibonacci]
        return self.sequence[n - 1]

    def set_upper_bound(self, upper_bound):
        if upper_bound < 1:
            raise NotSupportedException('')

        while self.sequence[-1] < upper_bound:
            self._calculate_next()

        # Discard any entries that are bigger than the upper bound
        while self.sequence[-1] > upper_bound:
            self.sequence.pop()

        # Return the last entry
        return self.sequence[-1]
