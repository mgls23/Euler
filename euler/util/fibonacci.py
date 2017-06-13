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
            raise NotSupportedException('')

        # See if that value has been calculated already
        while len(self.sequence) < n:
            self._calculate_next()

        # nth => n-1th in the list [0th of list is 1st Fibonnacci]
        return self.sequence[n - 1]

    def peek(self):
        return self.sequence[-1]

    def set_upper_bound(self, upper_bound):
        if upper_bound < 1:
            raise NotSupportedException('')

        while self.peek() < upper_bound:
            self._calculate_next()

        # Discard any entries that are bigger than the upper bound
        while self.peek() > upper_bound:
            self.sequence.pop(-1)

        # Return the last entry
        return self.peek()
